
# 직원 클래스
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def work(self):
        return f"{self.name}이(가) 일을 합니다."
           
# 객체(인스턴스) 1개 생성
employee1 = Employee("e1001","이순신")
print("아이디:", employee1.id)
print("이름:", employee1.name)
print(employee1.work())
print("========================")

#새 객체는 여러분 이름으로 만드세요(Id:e1002)
employee2 = Employee("e1002", "황보학")
print("아이디:", employee2.id)
print("이름:", employee2.name)
print(employee2.work())



