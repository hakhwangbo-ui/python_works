# 정수형 계산기 클래스
# 속성(변수) - 2개의수 : x, y
# 기능(함수) - 더하기, 빼기, 곱하기, 나누기

class Calculator:
    # 속성값 초기화
    def __init__(self):
        self.x = 0
        self.y = 0        

    #더하기
    def add(self, x, y):
        return x + y
    
    #빼기
    def sub(self, x, y):
        return x - y
    
    #곱하기
    def mul(self, x, y):
        return x * y
    
    #나누기
    def div(self, x, y):
        #분모가 0인경우 오류 처리
        if y == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        return x / y

# 객체 생성
cal = Calculator()
print(cal.add(10, 5))
print(cal.sub(10, 5))
print(cal.mul(10, 5))
print(cal.div(10, 0))
