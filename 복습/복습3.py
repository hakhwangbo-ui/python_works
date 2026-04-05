
# 리스트 - 여러개의 값을 저장
seasons = ["봄", "여름", "가을"]

print(seasons)
print(type(seasons)) #<class 'list'>

# 겨울을 리스트에 추가하세요 - append()
seasons.append("겨울")
print(seasons)

# 변경(수정) - 여름을 summer로 변경
seasons[1] = "summer"
print(seasons)

# 삭제 - remove() "가을"
seasons.remove("가을")
print(seasons) #['봄', 'summer', '겨울']

# 반복문 - for문
# "사랑해요"dmf 3번 반복하기
for i in range(3):
    print(f"{i}.사랑해요~♥")

# 1부터 10까지 출력
for i in range(1,11):
    print(i, end=' ')
print()

#1부터 10 까지 홀수 출력
for i in range(1,11):
    if (i % 2) != 0:
        print(i, end= ' ')
print()
# 1부터 10까지의 합계 계산
total = 0 # 합계를 저장할 변수 설정
for i in range(1,11):
    total += i
    print(f"i={i}, total={total}")
print("합계:", total)        
print("================")
# 국어 과목의 점수를 저장하는 리스트
# 국어 평균 = 총점 / 개수
scores = [80, 70, 95, 86]
count = len(scores) #개수
total = sum(scores) #총점
average = total / count #평균
max_val = max(scores) #최고점수
min_val = min(scores) #최저점수

print("개수:", count)
print("총점:", total)
# 소수 첫째자리까지 출력 -> 반올림-round()
print("평균:", round(average, 1))
print("최고점수:", max_val)
print("최저점수:", min_val)

#요소출력
sum_val = 0
for i in scores:
    sum_val += i #sum_val = sum_val + i
    print(i, end= ' ') #80 70 95 86
print()
print("총점:", sum_val)

# 소수점 이하 버림 - floor()는 math안에 있음
import math
money = 15000.3
money = math.floor(money)
print("금액:", money )



