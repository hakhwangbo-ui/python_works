# 리스트는 순서가 있고, 중복이 가능함
lst = [50, 20, 60, 70, 30, 20, 30]

print(len(lst)) #7

#리스트 안에 요소가 있는지 유무
print(60 in lst) #True
print(80 in lst) #False
print(80 not in lst) #True
# 맨 마지막 요소를 출력하세요
print(lst[-1])

#for문을 이용한 리스트 출력
for i in lst:
    print(i, end=' ')
print() #한 줄 차지

# 50보다 큰 요소만 출력하기
for i in lst:
    if i > 50:
        print(i, end= ' ')
print()
# 음식 분류 - 한식, 중식, 일식
foods = ["비빔밥", "자장면", "초밥","김치찌게"]

for food in foods:
    if food in ["자장면", "짬뽕"]:
        print(f"{food}는 중식입니다.")
    elif food in ["초밥","우동"]:
        print(f"{food}는 일식입니다")
    else:
        print(f"{food}는 한식입니다.")                


