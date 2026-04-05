# 중첩 for+
# range(초기값, 종료값 증감값) : 초기값을 생략하면 0이 됨
for i in range(1, 4):
    for j in (range(1, 5)):
        print("가", end ="")
    print()

# 3행 2열 반복
for i in range(3):
    for j in range(2):
        print(f"{i}, {j}")    
"""
i=0, j=0, 0, 0
     j=1, 0, 1
i=1, j=0, 1, 0
     j=1, 1, 1
i=2, j=0, 2, 0
     j=1, 2, 1           
"""        

# 구구단 전체 출력(2단 ~ 9단)
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()        


