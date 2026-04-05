# 함수(function) - 특정 작업을 수행하는 코드 묶음(블럭)
# def 키워드 사용
# 한 번 만들어서 여러 번 사용(재사용)할 수 있음
# return(반환)이 없는 함수
# 인사하기 함수 정의
def greet():
    print("Hello, World!")

#매개변수가 있는 함수
def greet2(name):
    print(f"Hello, {name}!")

# 구구단을 출력하는 함수
def get_gugudan(dan):
    for i in range(1, 10):
       print(f"{dan} x {1}")

# 함수 호출
greet()

greet2("Python")
greet2("명제")
get_gugudan(7)

# return(반환)이 있는 함수
def message():
    return "행운을 빌어요!"

# 제곱수를 정의하는 함수
def square(x):
    return x * x

#두 수의 차를 구하는 함수
def sub(a, b):
    return a- b


# return이 있으면 호출한 곳으로 값을 반환함
msg = message() # msg = "행운을 빌어요!"
print(msg)

value1 = square(5) #value1 = 25
print(value1) #25

value2 = sub(10, 20)
print(value2) #-10

# 사각형의 면적을 계산하는 함수
def square_area(w, h):
    s_area = w * h #지역변수
    return s_area

# 삼각형의 면적을 계산하는 함수
def triangle_area(b, h):
    tri_area = (b * h) / 2 #지역변수
    return tri_area

#print(s_area) #s_area는 호출된 후 소멸된 변수이다.(오류발생)
print("사각형 면적:", square_area(5, 4)) #사각형 면적: 20
print("삼각형 면적:", triangle_area(5, 4)) #삼각형 면적: 10.0

# 리스트를 매개 변수로 사용
"""
def times(a): # a = [1, 2, 3, 4]
    a2 = [] # 빈 리스트
    for i in a:
        a2.append(4 * i)
    return a2        

arr = [1, 2, 3, 4]
print(times(arr))
"""