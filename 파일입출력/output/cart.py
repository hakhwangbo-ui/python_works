
# 장바구니 리스트 저장하기
carts = ["달걀", "토마토", "쌀", "맥주", "사과"]

try:
    with open("./output/cart.txt", 'w', encoding='utf-8') as file:
        for item in carts:
            file.write(f"{item}\n")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

#catr.txt 읽기
try:
    with open("./output/cart.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print("FileNotFoundError", e)
