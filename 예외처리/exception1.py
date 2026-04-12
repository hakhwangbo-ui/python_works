# 1/ TypeError
try:
    print('20' + 20)
except TypeError as e:
    #print("TypeError:", e)   
    print("자료형 오류가 발행했습니다.", e)

# 2.ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError as e:
    #print("ZeroDivisionError:", e)    
    print("0으로 나눌 수 없습니다.", e)

# 3.NameError
try:
    message = 'Good Luck!' + friend    
except NameError as e:
    print("변수가 정의되지 않았습니다.", e)    

# 4.ValueError
try:
    number = int(input("숫자 입력: "))
    print(number + 5)
except ValueError as e:
    print("유효한 숫자를 입력하세요:", e)








