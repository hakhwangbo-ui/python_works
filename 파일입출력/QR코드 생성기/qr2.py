
# QR코드 생성기
# 설치가 안 되어 있다면 먼저 실행
#pip install qrcode[pil]
import qrcode

data = "http://www.naver.com"

#QR 코드 생성
img = qrcode.make(data)

#QR 코드 이미지 저장
img.save("naver_qr.png")
print("QR코드가 생성되었습니다.")