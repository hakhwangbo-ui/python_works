
# 파일에 구구단 쓰기

try:
    with open("output/gugudan-full.txt", 'w') as f:
        for i in range(2, 10):
            for j in range(1,10):
                f.write(f"{i} x {j} = {i*j}\n")
            f.write('\n')    
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 구구단 파일 읽기
try:
    with open("output/gugudan-full.txt", 'r') as f:
        gugudan = f.read()
        print(gugudan)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")