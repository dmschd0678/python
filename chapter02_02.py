# Chapter02 - 02
# 메소드 심화 2

# 일반적인 코딩
# 코드 반복

class Car():
    """
    Car Class
    2021/08/30
    """

    # 클래스 변수 (모든 인스턴스)

    car_count = 0
    def __init__(self, company, details):
        self._company = company
        self._details = details
        # self.car_count = 10
        Car.car_count += 1

    def __str__(self): # 사용자 입장 (print)
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)

    def detail_info(self):
        print("ID : {}".format(id(self)))
        print("Car Detail Info : {} {}\n".format(self._company, self._details.get("price")))

    def __del__(self):
        print("삭제")
        Car.car_count -= 1

# self -> 인스턴스 고유의 값을 저장하는 예약어
car1 = Car("Ferrari", {"color" : "White" ,"horsepower" : 400, "price" : 8000})
car2 = Car("Bmw", {"color" : "Black" ,"horsepower" : 270, "price" : 5000})
car3 = Car("Audi", {"color" : "Silver","horsepower" : 300,"price" : 6000})

print(id(car1))
print(id(car2))
print(id(car3))

print("\n")

print(car1._company == car2._company)
print(car1 is car2)

print("\n")

# dir & __dict__ 확인

print(dir(car1))
print(dir(car2))

print("\n")

print(car1.__dict__)
print(car2.__dict__)

#Doctring 주석 확인
print(Car.__doc__)

# 실행

car1.detail_info()
Car.detail_info(car1)

car2.detail_info()
Car.detail_info(car2)

car3.detail_info()
Car.detail_info(car3)

# Car.detail_info() 에러

#비교
print(car1.__class__ == car2.__class__)
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

print("\n")

# 클래스 변수
print(Car.car_count)
print(car1.__dir__())
print(car2.__dir__())

#접근
print(car1.car_count)
print(Car.car_count)

#삭제
del car2
print(Car.car_count)

# 인스터스 네임스페이스에 없으면 상위에서 검색
# 같은 이름으로 생성 가능 (인스턴스 검색 후 상위(클래스 변수, 부모 클래스 변수))