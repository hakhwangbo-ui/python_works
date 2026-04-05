
# 강아지 클래스
# 속성 - 종류(kind), 이름(name), 나이(age)
"""
class Dog:
    # 객체의 속성(생성자 매서드)
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def __str__(self):
        return f"종류:{self.kind}, 이름:{self.name}, ,나이:{self.age}"

# 인스턴스 생성
dog1 = Dog("말티즈","콩이",1)
dog2 = Dog("진돗개", "백구", 3)
print(dog1)
print(dog2)
"""           

class Dog2:
    kind = "진돗개" #클래스 변수
 
    # 객체의 속성(생성자 매서드)
    def __init__(self, name, age):
        self.name = name #인스턴스 변수
        self.age = age

    def __str__(self):
        #클래스 변수는 클래스 이름으로 직접 접근
        return f"종류:{Dog2.kind}, 이름:{self.name}, 나이:{self.age}"

# 인스턴스 생성
dog1 = Dog2("콩이", 1)
dog2 = Dog2("백구", 3)
print(dog1)
print(dog2)        