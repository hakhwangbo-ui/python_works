
import turtle as t # 별칭을 t로 사용

def polygon(n):
    t.color("red")
    for x in range(n):
        t.forward(100)
        t.left(360/n)

def polygon2(n, d):
    t.color("blue")
    for x in range(n):
        t.forward(d)
        t.left(360/n)

t.shape("turtle")

#함수 호출
polygon(5)
t.penup() #펜 올리기

#t.goto(0, 0) #현재위치
t.goto(200, 200)
t.pendown() #펜 내리기

polygon2(6, 60)

t.mainloop()

