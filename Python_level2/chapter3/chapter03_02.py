# Chapter 03 - 02
# 파이썬의 핵심 -> 시퀀스(sequence), 반복(Iterator), 함수(Fuction), 클래스 (Class)

# Special Method (Magic Method)
# 클래스 안에 정의할 수 있는 특별한(Built - in) 메소드

# 클래스 예제 2
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10

class Vector(object):
    def __init__(self, *arg):
        """
        Create a vector
        exaple : v = Vector(5, 10)
        """
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg
    def __repr__(self):
        """Retrun the Vector Informations."""
        return "Vector(%r, %r)" % (self._x, self._y)

    def __add__(self, other):
        """Return the Vector addition self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        if self._x == 0 and self._y == 0:
            print("warning 0,0")
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직 메소드 출력

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1))
print(bool(v3))