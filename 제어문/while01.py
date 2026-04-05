# while문 사용
"""
a = 1
print(1) #1

a += 1
print(a) #2

a += 1
print(a) # 3
"""
# 1 부터 5까지 출력
n = 1 #초기값
while n <= 5:
    print(n)
    n += 1 #증가값
print("==========")

# 5부터 1까지 출력
"""
n = 5
while n >= 1:
    print(n)
    n -= 1
"""
print("===============")
# 1부투 5까지의 합계 계산
n = 1
total = 0 #합계 저장 변수

while n <= 100:
    total = total + n
    print(f"n={n}, total= {total}")
    n += 1
print(f"합계: {total}")

