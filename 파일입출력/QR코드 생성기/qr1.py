
import tkinter as tk
from tkinter import messagebox
import qrcode

def make_qr():
    data = entry_data.get().strip()
    filename = entry_file.get().strip()

    if not data:
        messagebox.showwarning("입력 오류", "QR 코드에 넣을 내용을 입력하세요.")
        return

    if not filename:
        messagebox.showwarning("입력 오류", "파일 이름을 입력하세요.")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{filename}.png")

        messagebox.showinfo("완료", f"{filename}.png 파일로 저장되었습니다.")
        entry_data.delete(0, tk.END)
        entry_file.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("오류", f"QR 코드 생성 중 문제가 발생했습니다.\n{e}")

# 창 생성
window = tk.Tk()
window.title("QR 코드 생성기")
window.geometry("400x200")
window.resizable(False, False)

# 내용 입력
label_data = tk.Label(window, text="QR 내용 입력:")
label_data.pack(pady=5)

entry_data = tk.Entry(window, width=40)
entry_data.pack(pady=5)

# 파일명 입력
label_file = tk.Label(window, text="저장할 파일 이름:")
label_file.pack(pady=5)

entry_file = tk.Entry(window, width=40)
entry_file.pack(pady=5)

# 생성 버튼
btn_make = tk.Button(window, text="QR 코드 만들기", command=make_qr)
btn_make.pack(pady=15)

window.mainloop()