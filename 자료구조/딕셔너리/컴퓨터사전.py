# 컴퓨터 사전 만들기
#
print("♠ 컴퓨터 용어 사전 ♠")

dic = {
    "이진수": "0과 1로 이루어진 수의 체계",
    "변수": "데이터를 저장하기 위해 이름을 붙인 공간",
    "RAM": "Random Access Memory - 임의 접근 메모리",
    "CPU": "Central Processing Unit - 중앙 처리 장치"  
}

while True:
    word = input("검색할 용어 입력(종료: q or Q)")
    if word == "q" or word == "Q":
        print("프로그램을 종료합니다")
        break
    #definition = dic[word] #검색한 용어의 뜻(정의) #try~except
    definition = dic.get(word)
    if definition:
        print(f"{word}: {definition}")
    else:
        print(f"{word}는 사전에 없습니다")        



