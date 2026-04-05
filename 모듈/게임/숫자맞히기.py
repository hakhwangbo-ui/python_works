import random

answer = random.randint(1, 100)
count = 0

while True:
    try:
        user_input = int(input("1~100 사이의 숫자를 입력하세요: "))

        if user_input < 1 or user_input > 100:
            print("1~100 사이의 숫자만 입력해주세요.")
            continue

        count += 1

        if user_input < answer:
            print("↑ 더 큰 숫자입니다.")
        elif user_input > answer:
            print("↓ 더 작은 숫자입니다.")
        else:
            print(f"정답입니다! {count}회 만에 맞췄습니다.")
            print("게임을 종료합니다.")
            break

    except ValueError:
        print("숫자만 입력해주세요.")

try:
    user_input = int(input("1~100 사이의 숫자를 입력하세요: "))
except ValueError:
    print("숫자만 입력해주세요.")
