# 딕셔너리 -데이터를 **키(key)와 값(value)**의 쌍으로 저장하는 자료구조
# 딕셔너리는 {}를 사용
# 딕셔너리 생성
student = {
    'name' :"한강", 
    "age":21, 
    "university": "한강대학교"
}

print(student)
print(type(student)) #<class 'dict'>

# 요소에 접근(검색)
print(student["name"])

# 요소 조회(get(key)함수로 조회)
print(student.get("age"))

# 요소 수정
student["university"] = "남산대학교"
print(student)

# 요소 추가
student["major"] = "전자공학"
print(student)

# 요소 삭제 - pop(key)
student.pop("age")
print(student)

# 키, 값 확인
print(student.keys()) #dict_keys(['name', 'university', 'major'])
print(student.values()) #dict_values(['한강', '남산대학교', '전자공학'])

# 키, 값으로 전체 출력
for key in student.keys():
    print(f"{key}: {student[key]}")

