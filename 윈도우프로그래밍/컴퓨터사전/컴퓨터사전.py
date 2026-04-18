# 컴퓨터 용어 사전 만들기
from tkinter import *
dict = {
    "알고리즘": "문제를 해결하기 위한 일련의 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
    "변수": "데이터를 저장하는 공간",
    "이진수": "0과 1로 이루어진 수 체계",
}
def search():
    word = entry.get()
    definition = dict.get(word)
    if definition:
        output.config(text=f"{word}: {definition}")
    else:
        output.config(text=f"{word}는 사전에 없습니다")
        
window = Tk()
window.title("컴퓨터 용어 사전")

# 레이블 만들기
label = Label(window, text="컴퓨터 용어 사전") \
.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# 입력상자 만들기
entry = Entry(window, width=30)
entry.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# 버튼 만들기
button = Button(window, text="검색",command=lambda: search())
button.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# 결과 레이블 만들기
output = Label(window, width=40, height=10)
output.grid(row=3, column=0, padx=10, pady=10, sticky=W)




window.mainloop()