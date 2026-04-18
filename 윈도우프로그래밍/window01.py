
#  윈도우(창) 만들기
from tkinter import *

def click():
    #print("버튼이 클릭되었습니다.")
    output.config(text="안녕, 파이션")

window = Tk() #윈도우 객체 생성
window.title("윈도우(창) 만들기")

# 레이블 만들기
Label(window, text='안녕하세요').pack()
window.geometry("500x200") #whdth = 300px, height = 100px

# 버튼 이벤트(command에 함수 연결) 
Button(window, text="확인", command=click).pack()

# 클릭 후  출력 라벨
output = Label(window, text="")
output.pack()

window.mainloop() #윈도우 창 실행 유지