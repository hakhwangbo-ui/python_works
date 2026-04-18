#  
from tkinter import *

window = Tk()
window.title("Grid 레이아웃")
window.geometry("400x200")

# 레이블 만들기
Label(window, text='안녕하세요').grid(row=0, column=0, pady=10, padx=20)

# 버튼 만들기
Button(window, text='동').grid(row=0, column=1)
Button(window, text='서').grid(row=0, column=2)
Button(window, text='남').grid(row=1, column=1)
Button(window, text='북').grid(row=1, column=2)



window.mainloop()