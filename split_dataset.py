import os
import random
import shutil

# 원본 이미지 및 라벨 경로
image_dir = 'data_set/images'
label_dir = 'data_set/labels'

# train 및 val 데이터셋 경로
train_image_dir = 'data_set/train/images'
val_image_dir = 'data_set/val/images'
train_label_dir = 'data_set/train/labels'
val_label_dir = 'data_set/val/labels'

# 디렉터리 생성
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# 이미지 파일 목록 가져오기
image_files = os.listdir(image_dir)
random.shuffle(image_files)

# 80:20 비율로 나누기
split_ratio = 0.8
train_size = int(len(image_files) * split_ratio)

train_files = image_files[:train_size]
val_files = image_files[train_size:]

# 파일 복사
for file_name in train_files:
    shutil.copy(os.path.join(image_dir, file_name), train_image_dir)
    label_file = file_name.replace('.png', '.txt')
    shutil.copy(os.path.join(label_dir, label_file), train_label_dir)

for file_name in val_files:
    shutil.copy(os.path.join(image_dir, file_name), val_image_dir)
    label_file = file_name.replace('.png', '.txt')
    shutil.copy(os.path.join(label_dir, label_file), val_label_dir)

print(f'Total images: {len(image_files)}')
print(f'Train images: {len(train_files)}')
print(f'Validation images: {len(val_files)}')
