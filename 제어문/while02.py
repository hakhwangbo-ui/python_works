# 무한 반복문 - break
# 1부터 5까지 출력
n = 1
while True:
    if n > 5:
        break
    print(n)
    n += 1

# 1부터 5까지 합계
k = 1
total = 0

while True:
    if k > 5:
        break
    total += k
    k += 1
print(f"합계+: {total}")    

# 사용자에게 'y/n'을 입력되도록 반복하는 프로그램
while True:
    key = input("계속하려면 'y', 종료하려면 'n'을 입력하세요: ")
    if key == 'y' or key == 'Y':
        print("계속 진행합니다.")
    elif key == 'n' or key == 'N':
        print("반복을 종료합니다")        
        break
    else:
        print("올바른 입력이 아닙니다. 다시 시도하세요")