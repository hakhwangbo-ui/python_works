
# 파일 쓰기 - 텍스트만 가능
# with ~as - close() 생략해도 됨
try:
    with open("output/file02.txt", 'w', encoding='utf-8') as f:

        f.write("좋은 하루 되세요~\n")

        #f.wirte(100) #정수는 쓰기 불가
        f.write(str(100) + '\n')
        f.write(f"{str(200)}\n")
        f.write("Good Luck!")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


#파일 읽기
try:
    with open("output/file02.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")