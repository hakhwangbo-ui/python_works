
import turtle as t

def turn_right():
    t.setheading(0) #거불이  머리 방향이 0도 - 오른쪽
    t.forward(10)

def turn_up():
    t.setheading(90) # 위쪽 방행
    t.forward(10)

def turn_left():
    t.setheading(180) # 왼쪽 방행
    t.forward(10)

def turn_down():
    t.setheading(270) # 아래쪽 방행
    t.forward(10)    


t.shape("turtle")
#오른쪽 방향키 - Right , turn_right() 함수 호출
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen() # 키보드 입력 받을 준비






t.mainloop()