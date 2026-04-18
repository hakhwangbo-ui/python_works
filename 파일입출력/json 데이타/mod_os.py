# os 관련 모듈 사용
import os

# 현재 폴더(디렉토리) 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir) #C:\pyworks\파일입출력

# 폴더 목록 확인 -리스트 형태로 반환
items = os.listdir(current_dir)
print("디렉터리 내 항목:", items)

#새 디렉터리 생성
new_dir = os.path.join(current_dir, "new_folder")
os.mkdir(new_dir)
print("새 디렉터리 생성:", new_dir)




