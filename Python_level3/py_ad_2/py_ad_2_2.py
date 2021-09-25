"""
Chapter 2
Python Advanced(2) - Property(1) - Underscore
Keyword - access modifier(접근 지정자), underscore
"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
"""

# ex1

# Use underscore
# 1. 인터프리터, 2. 값 무시, 3. 네이밍(국제화, 자릿수)

# Unpacking
# 값 무시
x,_,y = (1,2,3)

a, *_, b = (1,2,3,4,5)

print('ex1 ->', x,y,a,b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    # print(_,val)
    pass

print()

# ex2

# 접근 지정자 : self.변수
# name : public
# _name : protected
# __name : private
# 파이썬 -> Public 강제 x. 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 X) -> Naming Mangling
# 타 클래스에서는 __변수 접근하지 않는 것이 원칙

# No use Property

class SampleA():
    def __int__(self):
        self.x =0
        self.__y = 0
        self._z = 0

a = SampleA()

a.x = 1

print('ex2 -> x : {}'.format(a.x))
# print('ex2 -> y : {}'.format(a.__y))
# print('ex2 -> z : {}'.format(a._z))

print('ex2 ->',dir(a))

a._SampleA_y = 34434    # 수정 가능하나 수정 권장 X
print('ex2 -> y : {}'.format(a._SampleA_y))

print()

# ex3
# 메소드 활용 Getter, Setter

class SampleB():
    def __init__(self):
        self.x = 0
        self.__y = 0    # _SampleB_y

    def get_y(self):
        return self.__y
    def set_y(self,value):
        self.__y = value

b = SampleB()

b.x = 1
b.set_y(2)

print('ex3 -> x : {}'.format(b.x))
print('ex3 -> y : {}'.format(b.get_y()))

# 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락
# b._SampleB__y = 343

print('ex3 ->',dir(b))
print('ex3 ->',b.__dir__())