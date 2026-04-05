
import time

#1970. 1. 1 자정이후 시간을 초로 환산
print(time.time()) #1775284956.2687557
print(time.time()) #1775285007.3630605

#수행 시간 측정 - sleep(초)
"""
print("3초후 메시지 출력")
time.sleep(3)
print("3초 경과함")

# 1부터 10까지 출력 - 1초 간격
for i in range(1,11):
    time.sleep(0.5)
    print(i)
"""    

# 1~ 100000까지의 합 계산
start_time = time.time()
 
#total = sum(range(1,10000001))
total = 0
for i in range(1,1000001):
    total += i

end_time = time.time()
print("합계:", total)
print("소요시간", end_time -  start_time, "초")

