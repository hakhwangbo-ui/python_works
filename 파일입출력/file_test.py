
# 파일 쓰기 - 텍스트만 가능
try:
    f = open("output/file01.txt", 'w', encoding='utf-8')

    f.write("좋은 하루 되세요~\n")

    #f.wirte(100) #정수는 쓰기 불가
    f.write(str(100))

    # 파일 닫기
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


#파일 읽기
try:
    f = open("output/file01.txt", 'r', encoding='utf-8')
    content = f.read()
    print(content)

    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")