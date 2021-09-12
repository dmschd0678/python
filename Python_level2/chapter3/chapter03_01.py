# Chapter 03 - 01
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(Iterator), 함수(Fuction), 클래스 (Class)

# Special Method (Magic Method)
# 클래스 안에 정의할 수 있는 특별한(Built - in) 메소드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100,n.__add__(100))
#print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print("\n")

# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit cClass info : {}, {}'.format(self._name,self._price)

    def __add__(self, x):
        print("__add__ 실행")
        return (self._price + x._price)

    def __sub__(self, x):
        print("__sub__ 실행")
        return self._price - x._price

    def __le__(self, x):
        print("__le__ 실행")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("__ge__ 실행")
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성

s1 = Fruit("Orange",7500)
s2 = Fruit("Banana", 3000)

#일반적인 계산
#print(s1._price + s2._price)


print(s1 + s2)
print(s1.__add__(s2))

# 매직 메소드
print(s1 >= s2)
print(s1 <= s2)

print(s1 - s2)
print(s2 - s1)

print(s1)
print(s2)