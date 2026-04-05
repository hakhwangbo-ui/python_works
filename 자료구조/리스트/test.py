# 변수
season = "봄"
print(season)

# 리스트
seasons = ["봄","여름","가을","겨울"]
print(seasons)

seasons[1] = "summer"
print(seasons[1])

seasons[3] = "winter"
print(seasons[3])
print(seasons[-1])

# 딕셔너리(key:value)
member = {'Tom':  13, "Jane": 9}

print(member["Jane"])

#요소 추가
member["Elsa"] = 10
print(member)

#요소 수정
member["Tom"] = 15
print(member)

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, end=' ')

print("\n------------------")

#변수로 출력(1부터 5까지)
for n in range(1,6,1):
    print(n, end=' ')



