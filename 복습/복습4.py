
# 함수
# 구구단 출력(단을 입력받아 출력)
"""
dan = int(input("단 입력: "))
for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")
"""
#  함수 형태
def get_gugu(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")

# 매개변수로 dan을 입력
value = int(input("단 입력: "))
get_gugu(value)





