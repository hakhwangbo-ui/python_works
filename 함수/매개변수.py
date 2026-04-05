
def greet(name, message="안녕하세요"):
    print(f"{name}님, {message}")

greet("민준","반갑습니다.")

# 기본 매개변수를 생략한 경우
greet("영우")

# 버스요금 함수
def take_bus(fare=1500):
    print(f"버스 요금은 {fare}원 입니다.")

take_bus()
take_bus(1700)



