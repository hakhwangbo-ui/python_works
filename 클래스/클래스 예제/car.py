"""
클래스 
 - 객체지향언어의 기본 개념으로 사물의 속성과 메서드를 하나의 단위로 묶는 틀이다.
 - 클래스는 설계도와 같고 이를 기반으로 여러 객체(인스턴스)를 생성할 수 있다.
 - 클래스의이름은 첫글자르 대문자로 시작함
"""

# 자동차 클래스 정의
"""
class Car:
    #속성
    color = "silver"
    wheels = 4

    # 매서드(함수)
    def drive(self):
        print("자동차가 달립니다.")

    def stop(self):
        print("자동차가 정지합니다.")


#객체(인스턴스) 생성 - car
#객체 = 클래스이름()
car = Car()
print("색상:", car.color)
print("바퀴 수:", car.wheels)
car.drive()
car.stop()
"""

class Bike:
    #생성자 매세드(필수)
    def __init__(self, color, gears):
        self.color = color
        self.gears = gears

    def ride(self):
        print(f"{self.color} 자전거가 {self.gears}단 기어로 달린다.")

    # 자전거의정보 - 매서드로 정의
    def get_info(self):
        return f"자전거 색상: {self.color}, 기어 수: {self.gears}"

#객체 생성
my_bike = Bike("검정색", 21)
#print("색상:", my_bike.color) #속성에 직접 접근은 권장하지 않음
#print("기어의 수:", my_bike.gears)
print(my_bike.get_info())
my_bike.ride()

your_bike = Bike("빨강색", 10)
print(your_bike.get_info())
your_bike.ride()

print("=============================")

# 객체 리스트

bikes = [
    Bike("초록색", 21),
    Bike("주황색", 10),
    Bike("white", 15)
]
#주황색 자전거 정보
print(bikes[1].get_info())
bikes[1].ride()

# 전체 출력
for bike in bikes:
    print(bike.get_info())
    bike.ride()













