"""" 
상속은 **상속(Inheritance)**은 기존에 만들어진 클래스(부모 클래스)의 
속성과 기능을 그대로 물려받아, 새로운 클래스(자식 클래스)를 만드는 것을 말합니다
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"안녕하세요, 저는 {self.name}입니다."

#Person을 상속받은 Employee 클래스
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    #소개 메서드 재정의(오버라이딩)
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} 제 사번은 {self.employee_id}입니다."        

person1 = Person("김부장")
print(person1.introduce())   

emp1 = Employee("이대리","e1001")
print(emp1.introduce())




