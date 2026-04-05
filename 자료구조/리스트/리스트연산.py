# 리스트 합계1
a = [10, 20, 30]
total = a[0] + a[1] + a[2]
print(total)

#for문을 이용한 리스트 합계
total = 0

for val in a:
    total += val
print(f"합계: {total}")    

# 평균 계산 : 합계 / 개수
average = total / len(a)
print(f"평균: {average}")