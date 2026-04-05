# 반복문 for
# range(시작값, 종료값, 증감값) 함수
# 종료값 -1이 리스트에 저장됨
# list(순서열) gkatn
print(range(1, 5, 1)) #range(1, 5)
print(list(range(1, 5, 1))) #[1, 2, 3, 4]
print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11, 2))) #[1, 3, 5, 7, 9]

# 1부터 10까지 출력
for n in range(1, 11):
    print(n)
print("================")    
# 1부터 10까지 짝수 출력
# 짝수는 어떤 수를 2로 나눈 나머지가 0이다.(n % @ == 0)  
for n in range(1, 11):
    if n % 2 == 0:
        print(n) # 2, 4, 6, 8 ,10

# range()만 사용해서 짝수만 출력
for n in range(2,11,2):
    print(n) # 2, 4, 6, 8 ,10

#단을 입력 받아 구구단 출력하기
# 3 * 1 = 3
#dan = 3
dan = int(input("단을 입력하세요"))

for i in range(1, 10, 1):
    print(f"{dan} x {i} = {dan*i}")



         
