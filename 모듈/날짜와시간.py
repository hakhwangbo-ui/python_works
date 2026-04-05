# 날짜와 시간 다루기
from datetime import datetime, date

#현재 날짜와 시간
now = datetime.now()
print(now) #2026-03-29 16:13:21.643770

# 년 월 일
print(f"{now.year}년 {now.month}월 {now.day}일")

# 시 분 초
print(f"{now.hour}:{now.minute}:{now.second}")

# 오늘 날짜 - date()
today = date.today()
print(today)

# 식목일
the_day = date(2026,4, 5)
print("식목일:", the_day)

# 날짜 차이 계산
date_diff = the_day - today
print("D-day:", date_diff.days)




