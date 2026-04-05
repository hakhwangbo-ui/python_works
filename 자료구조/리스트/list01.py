# 리스트 - 여러개의 데이터를 순서대로 저장하는 자료구조 
# 
my_list = [10, 20, 30, 40]
print(my_list)
print(type(my_list)) # <class 'list'>

# 요소에 접근(검색)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[-1])
print(my_list[-2])

# 요소 변경
my_list[1] = 200
print(my_list)

# 요소 추가 -append(요소) : 맨 뒤에서 추가
my_list.append(50)
print(my_list) #[10, 200, 30, 40, 50]

# 요소 삭제 - del / pop()
del my_list[2] #30을 삭제
print(my_list) #[10, 200, 40, 50]

# 맨 위에서 삭제 - pop()
my_list.pop()
print(my_list) #[10, 200, 40]

# 문자형 리스트
carts = ["라면","달걀","토마토","커피"]

# 리스트의 길이(크리) - len(리스트)
print(len(carts)) #4

# 요소 조회
# "토마토" 를 선택해서 출력하세요
print(carts[2])

# "커피"를 "콜라"로 변경하세요
carts[3] = "콜라"
print(carts)  #['라면', '달결', '토마토', '콜라']

# 삭제 - remove(요소)
carts.remove("달걀")
print(carts) #['라면', '토마토', '콜라']

