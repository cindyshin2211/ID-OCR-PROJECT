# 신분증 인식 OCR 프로젝트(ID Card Recognition OCR Project)

## 📝 프로젝트 개요(Project Overview)
이 프로젝트는 리포팅 툴 및 전자 계약 솔루션을 제공하는 회사에서 인턴으로 수행한 프로젝트입니다. 본 프로젝트의 목표는 신분증을 인식하고 해당 신분증에서 필요한 정보를 추출하는 기능을 구현하는 것입니다. 이 프로젝트는 완벽한 기능을 갖추지는 않았지만, 신분증 인식 기능을 구현하기 위한 end to end 프로젝트로써의 의미를 지닙니다. 특히, 프로젝트를 수행하면서 발견한 여러 가지 고려 사항들이 향후 실제 프로젝트에서 유용하게 활용되기를 기대합니다.

#### 프로젝트 목표(Project Objectives)
- 신분증 인식을 위한 기초적인 기능 개발 및 회사 제품과의 통합 가능성 탐색
- 이미지 처리, 데이터 라벨링, 모델 학습 등의 신분증 처리 관련 문제 탐구
- 합성 신분증 데이터를 생성하고 이를 바탕으로 모델 학습 및 간단한 신분증 정보 추출 기능 개발
  
본 프로젝트는 데이터 생성부터 모델 학습, 간단한 정보 추출까지 이어지는 파이프라인을 구축하며, 최종 배포 준비 단계까지는 아니지만 향후 발전을 위한 중요한 기초를 제공합니다.

## 🗂 폴더 구조(Folder Structure)
```
IDCARD
|
data_set/
│   ├── data_imprinting/
│   ├── face_image_making/
│   ├── image_synthesis/
│   ├── images/
│   ├── labels/
│   ├── test/
│   ├── train/
│   └── val/
idcard_data_making/
│   ├── data_imprinting.ipynb
│   ├── data_making1.ipynb
│   ├── data_making2.ipynb
│   ├── face_image_making.ipynb
│   └── image_synthesis.ipynb
static/
│   ├── css/
│   └── uploads/
templates/
│   └── index.html
yolov5/
app.py
README.md
split_dataset.py
requirements.txt
```
#### 주요 폴더 및 파일 설명(Key Folders and File Description)
- data_set/: 본 프로젝트에서 사용한 데이터가 모두 포함되어 있으며, 신분증 이미지 합성에 사용된 이미지 데이터와 신분증 라벨링을 통해 학습한 모델 데이터를 포함합니다.
  - data_imprinting/,face_image_making/, image_synthesis/: 신분증 데이터를 생성하기 위한 이미지 파일들로, idcard_data_making/에 같은 이름으로 사용한 코드들이 작성되어있습니다.
  - images/, labels/, train/, test/, val/: 모델 학습에 사용된 신분증 데이터셋 및 데이터 분할 구조입니다.
- idcard_data_making/: 합성 신분증 데이터를 생성하는 과정을 설명하는 Jupyter 노트북 파일들이 위치합니다. <b>이 폴더 내의 모든 코드는 구글 코랩에서 작성하였으므로 향후 다른 데이터셋을 통합개발환경에서 생성할 시 코드 변경이 필요합니다.</b>
  - data_imprinting.ipynb: 빈 신분증을 생성하는 코드
  - face_image_making.ipynb: 신분증에 사용될 얼굴 이미지를 생성하는 코드
  - image_synthesis.ipynb: 최종적으로 신분증 이미지를 합성하는 과정을 설명하는 코드
  - data_making1.ipynb, data_making2.ipynb: 신분증 데이터의 다양성 확보를 위해 원본이미지를 변형하는 코드
- yolov5/: 신분증 인식 작업에 사용된 YOLOv5 객체 탐지 모델 관련 파일들이 포함되어 있습니다.

- split_dataset.py: 데이터셋을 학습, 검증, 테스트 세트로 나누는 스크립트입니다.

- app.py: 신분증 인식 모델을 사용해 웹 애플리케이션 데모를 실행하는 백엔드 코드입니다.

## 🚀 설치(Installation)
https://github.com/cindyshin2211/ID-OCR-PROJECT.git을 설치하여 실행하려면 다음 단계에 따르세요
1. 저장소를 클론합니다.
   ```
   git clone https://github.com/cindyshin2211/ID-OCR-PROJECT.git
   ```
2. 필요한 패키지를 설치합니다.
   ```
   pip install -r requirements.txt
   ```
3. flask 서버 실행
   ```
   python app.py
   ```
## 🎥 데모(Demo)

https://github.com/user-attachments/assets/2b78bea8-330e-4f1b-8602-2b561c1c4d55

## 🌱 발전 가능성 및 개선 사항(Potential Improvements)
이 프로젝트는 기초적인 파이프라인을 구축하였으며, 다음과 같은 부분에서 추가적인 발전이 필요합니다.

- 정확도 향상: 현재 모델은 시범적으로 작동하는 상태이며, 데이터의 다양성 확보, 현실과 비슷한 데이터 셋 마련, 텍스트 인식 모델 성능 향상 등을 통해 정확도를 높일 수 있습니다.
- 모델 배포: 현재는 Flask 앱을 이용한 간단한 데모이지만, 이를 클라우드 기반 서비스로 확장하는 작업이 필요합니다.

