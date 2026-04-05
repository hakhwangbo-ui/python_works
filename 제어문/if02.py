# if 중첩
"""
num = 17

if num > 10:
    if num < 20:
        print("10보다 크고 20보다 작은 수 입니다.")
    else:
        print("20 이상의 수입니다.")
else:
    print("10 이하의 수 입니다.")
"""
    
# 윤년을 판별하는 프로그램
# 4년마다 주기적으로 있다
# 100으로 나누어 떨어지면 윤년이 아님
# year = 2000 #숫자
year = int(input("연도를 입력하세요."))
     
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")    


        