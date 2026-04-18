# 
import tkinter as tk
from tkinter import messagebox

# 컴퓨터 용어사전 데이터
computer_dict = {
    "cpu": "컴퓨터의 중앙처리장치로, 명령을 해석하고 실행하는 장치입니다.",
    "ram": "현재 실행 중인 프로그램과 데이터를 임시로 저장하는 주기억장치입니다.",
    "rom": "읽기 전용 메모리로, 주로 변경되지 않는 정보를 저장합니다.",
    "ssd": "반도체를 이용해 데이터를 저장하는 장치로, 속도가 빠릅니다.",
    "hdd": "자기 디스크를 이용해 데이터를 저장하는 장치입니다.",
    "gpu": "그래픽 처리 장치로, 영상 처리와 게임, AI 연산 등에 사용됩니다.",
    "os": "운영체제로, 컴퓨터 하드웨어와 소프트웨어를 관리하는 시스템입니다.",
    "python": "쉽고 강력한 프로그래밍 언어입니다.",
    "algorithm": "문제를 해결하기 위한 절차나 방법입니다.",
    "database": "데이터를 체계적으로 저장하고 관리하는 시스템입니다.",
    "network": "컴퓨터와 장치들이 서로 연결되어 데이터를 주고받는 구조입니다.",
    "server": "다른 컴퓨터에 서비스나 데이터를 제공하는 컴퓨터입니다.",
    "client": "서버에 요청을 보내 서비스를 받는 컴퓨터나 프로그램입니다.",
    "compiler": "프로그래밍 언어로 작성한 코드를 기계어로 번역하는 프로그램입니다.",
    "bug": "프로그램의 오류나 결함을 의미합니다."
}

# 검색 함수
def search_word():
    word = entry.get().lower().strip()

    if word == "":
        messagebox.showwarning("입력 오류", "검색할 용어를 입력하세요.")
        return

    if word in computer_dict:
        result_label.config(text=f"[{word}]의 뜻:\n{computer_dict[word]}")
    else:
        result_label.config(text=f"'{word}'는 사전에 없는 용어입니다.")

# 메인 창 생성
window = tk.Tk()
window.title("컴퓨터 용어사전")
window.geometry("500x300")
window.resizable(False, False)

# 제목 라벨
title_label = tk.Label(window, text="컴퓨터 용어사전", font=("맑은 고딕", 16, "bold"))
title_label.pack(pady=10)

# 입력 안내 라벨
guide_label = tk.Label(window, text="검색할 컴퓨터 용어를 입력하세요:", font=("맑은 고딕", 11))
guide_label.pack()

# 입력창
entry = tk.Entry(window, font=("맑은 고딕", 12), width=30)
entry.pack(pady=10)

# 버튼 프레임
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

# 검색 버튼
search_button = tk.Button(button_frame, text="검색", font=("맑은 고딕", 11), width=10, command=search_word)
search_button.grid(row=0, column=0, padx=5)

# 종료 버튼
exit_button = tk.Button(button_frame, text="종료", font=("맑은 고딕", 11), width=10, command=window.quit)
exit_button.grid(row=0, column=1, padx=5)

# 결과 출력 라벨
result_label = tk.Label(window, text="", font=("맑은 고딕", 11), wraplength=450, justify="left")
result_label.pack(pady=20)

# 엔터키로 검색 가능하게 설정
window.bind("<Return>", lambda event: search_word())

# 실행
window.mainloop()