# 컴퓨터 용어 사전 만들기 (단어 등록 기능 추가)
from tkinter import *
dictionary = {
    "알고리즘": "문제를 해결하기 위한 일련의 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
    "변수": "데이터를 저장하는 공간",
    "이진수": "0과 1로 이루어진 수 체계",
}

def search():
    word = entry.get()
    definition = dictionary.get(word)
    output.delete(1.0, END)
    if definition:
        output.insert(END, f"{word}: {definition}")
    else:
        output.insert(END, f"{word}는 사전에 없습니다")

def add_word():
    word = entry_word.get()
    definition = entry_def.get()
    if word and definition:
        dictionary[word] = definition
        output.delete(1.0, END)
        output.insert(END, f"{word}가 등록되었습니다.")
        entry_word.delete(0, END)
        entry_def.delete(0, END)
    else:
        output.delete(1.0, END)
        output.insert(END, "단어와 정의를 모두 입력하세요.")

window = Tk()
window.title("컴퓨터 용어 사전")

# 레이블 만들기
label = Label(window, text="컴퓨터 용어 사전") \
.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# 검색 입력상자 만들기
entry = Entry(window, width=30)
entry.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# 검색 버튼 만들기
button = Button(window, text="검색", command=lambda: search())
button.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# 결과 박스 만들기
output = Text(window, width=40, height=10)
output.grid(row=3, column=0, padx=10, pady=10, sticky=W)

# 단어 등록 레이블
label_word = Label(window, text="새 단어 등록")
label_word.grid(row=4, column=0, padx=10, pady=5, sticky=W)

# 단어 입력상자
entry_word = Entry(window, width=30)
entry_word.grid(row=5, column=0, padx=10, pady=10, sticky=W)

# 정의 입력상자 레이블
label_def = Label(window, text="정의")
label_def.grid(row=6, column=0, padx=10, pady=5, sticky=W)

# 정의 입력상자
entry_def = Entry(window, width=30)
entry_def.grid(row=7, column=0, padx=10, pady=10, sticky=W)

# 등록 버튼 만들기
button_add = Button(window, text="등록", command=lambda: add_word())
button_add.grid(row=8, column=0, padx=10, pady=10, sticky=W)

window.mainloop()