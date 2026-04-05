import turtle

t = turtle.Turtle()  # 거북이 객체 생성
t.shape("turtle")    # 커서 모양을 거북이로 변경

"""
turtle.shape("turtle")
turtle.forward(100) #100 필셀만큼 직진
turtle.right(90) #오른쪽으로 90도 방향
turtle.forward(100)
turtle.right(90) #오른쪽으로 90도 방향
turtle.forward(100)
turtle.right(90) #오른쪽으로 90도 방향
turtle.forward(100)
turtle.right(90) #오른쪽으로 90도 방향
turtle.mainloop() #윈도우(창) 계속 유지
"""
"""
turtle.color("blue")
#반복문 사용
for i in range(4):
    turtle.forward(100)
    turtle.right(90) #오른쪽으로 90도 방향

turtle.color("red")
for i in range(3):
    turtle.forward(100)
    turtle.left(120) #오른쪽으로 90도 방향
"""
turtle.color("blue")
turtle.pensize(2)
n = 4 #변의 갯수
d = 150 #거리(distanse)

#사각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)

turtle.color("red")
turtle.pensize(3)
n = 3 #변의 갯수
d = 75 #거리(distanse)

#삼각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)

#원
turtle.color("black")
turtle.circle(50) #반지름 - 50픽셀




turtle.mainloop() #윈도우 창 계속 유지