print("***간단한 규칙 기반 챗봇***")

def my_chatbot():
    while True:
        user_input = input("챗봇에게 질문하세요.(종료: 'exit/quit' 입력)")
        if user_input in["exit", "quit"]:
            print("챗봇을 종료합니다.")
            break
        elif "안녕" in user_input:
            print("챗봇: 안녕하세요, 무엇을 도와드릴까요?")
        elif "이름" in user_input:
            print("챗봇: 제 이름은 챗봇입니다.")       
        else:
            print("챗봇: 죄송합니다. 잘모르겠어요.")    

# 실행
my_chatbot()
