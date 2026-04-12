# 파일을 생성

# 파일 열기 - open(경로, 모드)
f = open("c:/pyfile/file1.txt", 'w')

# 파일에 문자열 작성 - write()
f.write("Hello~ Python!\n")
f.write("좋은 하루 되세요.\n")

#숫자는 저장할 수 없고, 문자열로 변환하여 작성
#f.write(30)
f.write(str(30) + '\n')

# 파일 종료(닫기) - close()
f.close()
