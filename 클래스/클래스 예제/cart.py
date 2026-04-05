
# 쇼핑물 장바구니 클래스 정의
class Cart:
    #생성자 메서드
    def __init__(self):
        self.items = [] #빈 리스트
        
    #아이템 추가 메서드
    def add_item(self, item):    
        self.items.append(item)

    # 아이템 삭제 메서드
    def remove_item(self, item):
        self.items.remove(item)

    # 아이템 조회 메서드    
    def get_items(self):
        return f"장바구니: {self.items}"        

# 객체 생성
cart = Cart()

#아이템 추가
cart.add_item("쌀")
cart.add_item("달걀")
cart.add_item("토마토")

cart.remove_item("달걀")

#아이템 목록 출력
print(cart.get_items()) #장바구니: ['쌀', '달걀']


