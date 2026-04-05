
# 변수 이름 - season, 계절 : 봄
season = "봄"
print(f"계절은 {season}입니다.")
print(type(season)) #<class 'str'>

n = 10
print(f"숫자는 {n}입니다.")

# n 변수에 20을 더하세요.
n += 20
print(f"n = {n}")
print(type(n)) #<class 'int'>

#원의 둘레를 계산(2 x 원주율 x 반지름 )
pi = 3.14
radius = 6
print(type(pi)) #<class 'float'>

#계산 공신
result = 2 * pi * radius
print(f"월의 둘레는{result}입니다.")

# 정밀한 계산 - 수학 모듈(math)

import math

PI = math.pi
redius = 10
print(f"원주율은{PI}입니다.")

# 정밀한 원의 둘레
result2 = 2 * PI * radius
print(f"새로운 원의 둘레는 {result2}입니다.")
