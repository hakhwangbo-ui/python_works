# 학생 성적표 출력
student_list = [
    {"name" : '이대한', 'kor' : 95, 'eng': 80},
    {"name" : '박민국', 'kor' : 80, 'eng': 75},
    {"name" : '오상식', 'kor' : 90, 'eng': 80},
]
print("첫번째요소:", student_list[0]) #{'name': '이대한', 'kor': 95, 'eng': 80}
print(student_list[0]["name"]) #이대한
print(student_list[0]["kor"])  #95


# 전체 선택
print("========학생 성적표 =========")
print("이름\t국어\t영어\t평균")
for student in student_list:
    #print(student["name"], '\t', student["kor"], '\t', student["eng"])
    name = student["name"]
    kor = student["kor"]
    eng = student["eng"]
    avg = (kor + eng) / 2 # 평균 = 총점/개수
    #print(f"{student['name']}\t{student['kor']}\t{student['eng']}")
    print(f"{name}\t{kor}\t{eng}\t{avg:.2f}")


