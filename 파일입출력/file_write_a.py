# 파일을 생성

# 파일 열기 - open(경로, 추가모드)
f = open("c:/pyfile/file1.txt", 'a')

# 파일에 문자열 작성 - write()
f.write("사랑해요")

# 파일 종료(닫기) - close()
f.close()
