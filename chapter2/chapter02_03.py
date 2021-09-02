# Chapter02 - 03
# 메소드 심화 3
# 일반적인 코딩
# 코드 반복

"""
Method
Instance    : self
Class       : cls
Static      : X
"""

class Car():
    """
    Car Class
    2021/08/31
    Descroption : Class Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 사용자 입장 (print)
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)

    # Instance Method
    # self : 객체 고유의 속성 값을 사용
    def detail_info(self):
        print("ID : {}".format(id(self)))
        print("Car Detail Info : {} {}\n".format(self._company, self._details.get("price")))

    # Instance Method
    def get_price(self):
        return "Before Car Price - > company : {}, price : {}".format(self._company,self._details.get("price"))

    # Instance Method
    def get_price_culc(self):
        return "Before Car Price - > company : {}, price : {}".format(self._company,self._details.get("price") * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("더 높은 값을 ")
            return
        cls.price_per_raise = per
        print("성공\n가격이 증가됨\n")

    # Static Method 잘 안 씀!
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return "확인 : 이 차는 {}입니다.".format(inst._company)
        return "이 차는 BMW가 아닙니다"

# self -> 인스턴스 고유의 값을 저장하는 예약어
car1 = Car("Ferrari", {"color" : "White" ,"horsepower" : 400, "price" : 8000})
car2 = Car("Bmw", {"color" : "Black" ,"horsepower" : 270, "price" : 5000})

# 전체 정보
print("전체 정보")
car1.detail_info()
car2.detail_info()

# 가격 정보 (직접 접근)
print("가격 정보 (직접 접근)")
print(car1._details.get("price"))
print(car2._details.get("price"))

print()

# 가격 정보 (인상 전)
print("가격 정보 (인상 전)")
print(car1._details.get("price"))
print(car2._details.get("price"))

print()

# 가격 인상 (클래스 메소드 사용 X)
Car.price_per_raise = 1.4

# 가격 정보 (인상 후)
print("가격 정보 (클래스 메소드 사용 X)")
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# 가격 인상 (클래스 메소드)
Car.raise_price(1.6)
print("가격 정보")
print(car1.get_price_culc())
print(car2.get_price_culc())

print()

# 인스턴스 호출 static
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 아래 있는 코드도 작동 가능
# print(car2.is_bmw(car1))

# 클래스 호출 static
# print(Car.is_bmw(car2))

