#객체의 정보를 출력하는 함수 - __str__()

class Student:
    #생성자 메서드(속성-학번, 이름)
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    # 객체의 문자열 정보        
    def __str__(self):
        return f"학번: {self.student_id}, 이름:{self.name}"

# 객체 생성
student1 = Student("20260101","우영우")     
print(student1)
print("=======================")

# 객체 리스트
students = [
    Student("s1001", "이순신"),
    Student("s1002", "고담덕"),
    Student("s1003", "한강")
]
# '한강' 학생의 정보를 출력하세요
print(students[2])

# 학생 명단
print("**** 학생 명단 *****")

for student in students:
    print(f"{student}")

