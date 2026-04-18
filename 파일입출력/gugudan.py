
# 파일에 구구단 쓰기

try:
    with open("output/gugudan.txt", 'w') as f:
        dan = 7
        for i in range(1,10):
            f.write(f"{dan} x {i} = {dan*i}\n")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 구구단 파일 읽기
try:
    with open("output/gugudan.txt", 'r') as f:
        gugudan = f.read()
        print(gugudan)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")