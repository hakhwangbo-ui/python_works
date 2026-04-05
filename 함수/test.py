

# 함수 정의
def add(x, y):
    sum = x + y #sum -> 지역변수
    return sum  #호출한 곳으로 보내줌(반환)

#함수 호출
result = add(4,5)
print(result) #9
arr = [3, 6, 9]
# 합계 -sum()
print(sum(arr))

# 직접 리스트 합계
"""
sum_n = 0 #합계 저장 변수
for n in arr:
    sum_n = sum_n + n
    print("n=", n, ", sum_n =", sum_n)

print(sum_n) #18
"""
# 함수
def sum_n(arr): #arr= v
    total = 0
    for n in arr:
        total +=  n #total = total + n
    return total        

v = [1, 2, 3, 4]
print(sum_n(v))


