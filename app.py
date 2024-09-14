from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import torch
import re
import easyocr  # EasyOCR 추가
import pytesseract  # Tesseract OCR 추가

# YOLOv5 모델 로드 (가장 간단한 방법)
model = torch.hub.load('yolov5', 'custom', path='./yolov5/runs/train/exp/weights/best.pt', source='local')

# Flask 애플리케이션 초기화
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'} 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
# EasyOCR 리더 초기화 (한국어와 영어 지원)
reader = easyocr.Reader(['ko', 'en'])

# 텍스트 추출 함수 정의
def extract_text(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image file could not be loaded. The file might be corrupted or in an unsupported format.")
    
    results = model(img)

    class_names = results.names
    target_classes = ['name', 'id_number', 'issue_date']
    extracted_text = {}

    for *box, conf, cls in results.xyxy[0]:
        class_name = class_names[int(cls)]
        
        if class_name in target_classes:
            x1, y1, x2, y2 = map(int, box)
            cropped_img = img[y1:y2, x1:x2]


            if class_name == 'issue_date' or class_name=='id_number':
                cropped_img_gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
                _, cropped_img_thresh = cv2.threshold(cropped_img_gray, 150, 255, cv2.THRESH_BINARY)
                custom_config = r'--oem 3 --psm 6'
                text = pytesseract.image_to_string(cropped_img_thresh, lang='eng', config=custom_config).strip()
                if class_name=='issue_date':
                    text = re.sub(r'[^0-9.]', '', text)
                else:
                    text = re.sub(r'[^0-9-]', '', text)
                
            else:# EasyOCR을 사용하여 텍스트 추출
                ocr_result = reader.readtext(cropped_img)
            
                if ocr_result:
                    text = ocr_result[0][1].strip()  # 인식된 텍스트 (ocr_result[0][1]에 텍스트가 있음)
                
                    # 텍스트 후처리
                    if class_name == 'name':
                        text = re.sub(r'[^가-힣\s]', '', text)
                
            
                
            extracted_text[class_name] = text
    
    return extracted_text

# 루트 경로 - 파일 업로드 및 결과 표시
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                

                # 텍스트 추출
                extracted_text = extract_text(filepath)
                print(extracted_text)
                
                return render_template('index.html', extracted_text=extracted_text, filepath=filepath)
            
        return render_template('index.html')
    except Exception as e:
        print({e})
        return render_template('index.html', error_message=str(e))  # 오류 발생 시에도 index.html을 렌더링

# 웹 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
