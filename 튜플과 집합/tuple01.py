# 튜플 - 수정할 수 없는 리스트
t1 = (1, 2, 3)
print(t1) #(1, 2, 3)
print(type(t1)) #<class 'tuple'>

# 특정 요소 접근(조회)
print(t1[1]) #2
print(t1[-1]) #3

# 요소 삭제
# del t1[0] #삭제 불가

# 요소 수정
# t1[-1] = 5 #수정 불가

# t1의 합계
print("합계:", sum(t1))

# 전체 요소 출력
for i in t1:
    print(i)

# 단일 요소를 가진 튜플
#t2 = (4)  #정수3
#print(type(t2)) #<class 'int'>   
t2 = (4,)
print(type(t2)) #<class 'tuple'>
print(t2) 

# 튜플 연결
t3 = t1 + t2
print(t3) #(1, 2, 3, 4)

# 튜플의 사용
# 점수 저장
scores = []
#scores.append(80) #리스트의 요소
scores.append((80,))
scores.append((90,))
print(scores) #[(80,), (90,)]#[('국어', 90)] 

#과목과 점수 입력
subjects = []

subjects.append(("국어", 90))
subjects.append(("수학", 80))
print(subjects) #[('국어', 90), ('수학', 80)]

"""
[
    ('국어', 90), 
    ('수학', 80)
]
"""

# 특정 요소 조회
print(subjects[0])
print(subjects[1])

#이차원 검색(0행0열, 0행1열)
print(subjects[0][0])
print(subjects[0][1])

# 은행 - 입금, 출금
transactions = []
transactions.append(("입금", 20000))
transactions.append(("출금", 10000))
print(transactions)

for transaction in transactions:
    print(f"{transaction[0]}: {transaction[1]}")





