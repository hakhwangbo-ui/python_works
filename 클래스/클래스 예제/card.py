# 카드 번호를 생성하는 클래스
"""
class Card:
    #생성자 메서드
    def __init__(self, owner):
        self.card_number = 1000
        self.card_number= self.card_number + 1
        self.owner = owner #소유자


#객체 생성
card1 = Card("장그래")    
print(card1.card_number) #1001
print(card1.owner)

card2 = Card("김대리")
print(card2.card_number) #1001
"""
class Card:
    card_number = 1000 #클래스 변수
    #생성자 메서드
    def __init__(self, owner):
        # Card 클래스 이름으로 직접 접근
        Card.card_number= Card.card_number + 1

        #인스턴스 변수에 현재 카드번호 저장
        self.card_number = Card.card_number
        self.owner = owner #소유자


#객체 생성
card1 = Card("장그래")    
print(card1.card_number) #1001
print(card1.owner)

card2 = Card("김대리")
print(card2.card_number) #1002

card3 = Card("오상식")
print(card3.card_number) #1003

# 문자열 더하기
class City:
    #클래스 리스트
    a = ["Seoul","Incheon","Daejon","Jeju"]

str = ""
for i in City.a:
    str += i[0]

print(str)             

