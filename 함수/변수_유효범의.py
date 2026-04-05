"""
전역변수
 메인 함수 영역에 선언하여 사용하고, 영향 범위가 전체로 미친다
 프로그램이 종료되면 메모리에서 소멸한다
"""
# 전역 변수의 유효 범위
quantity = 2 #수량, 전역변수
def get_price():
    # 금액 = 가격 * 수량
    price = 1000 * quantity # 지역변수
    print(f"{quantity}개에 {price}원 입니다.")

get_price() #함수 호출

"""
지역변수
지역변수는 함수나 명령문(조건, 반복)의 블록 안에서 생성되며,
블록{ }을 벗어나면 메모리에서 소멸한다.
"""
def click_a():
    x = 0  # 지역변수
    x += 1
    print("x =", x)

click_a() # x=1
click_a() # x=1
click_a() # x=1

"""
정적변수
global 키워드를 붙이면 전역변수화 함
값을 공유하고, 유지하며,
프로그램이 종료되면 소멸한다.
"""
def click_b():
    global x #지역변수가 전역변수화 함
    x += 1
    print("x=", x)

x = 0 #전역변수
click_b() # x = 1
click_b() # x = 2
click_b() # x = 3
