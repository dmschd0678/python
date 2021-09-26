"""
Chapter 2
Python Advanced(2) - Method Overriding
Keyword - Overriding, OOP, 다형성
"""
"""
메소드 오버라이딩 효과
1. 서브 클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능(구조적 접근)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류 가능성 감소, 메소드 이름 절약, 유지보수성 증가 등
"""

# ex1
# 기본 Overriding 예제

class ParentEx1():
    def __init__(self):
        self.value = 5
    def get_value(self):
        return self.value

class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

# 부모 클래스 메소드 호출
print('ex1 ->',c1.get_value())

# c1 모든 속성 출력
print('ex1 ->',dir(c1))

# 부모 & 자식 모든 속성 출력
print('ex1 ->',dir(ParentEx1))
print('ex1 ->',dir(ChildEx1))

print()

print('ex1 ->',ParentEx1.__dict__)
print('ex1 ->',ChildEx1.__dict__)

# ex2
# 기본 Overriding 메소드 재정의

class ParentEx2():
    def __init__(self):
        self.value = 5
    def get_value(self):
        return self.value

class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()

# 자식 메소드 재정의 후 호출
print('ex2 ->',c2.get_value())

# ex3
# Overriding 다형성 예제

import datetime

class Logger():
    def log(self,msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self,msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now(),msg = msg)
        super(TimestampLogger, self).log(message)
        # super().log(message)

class DateLogger(Logger):
    def log(self,msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now().strftime('%Y-%m-%d'),msg = msg)
        # super(DateLogger, self).log(message)
        super().log(message)
l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메소드 재정의 실습
print('ex3 ->',l.log('Called logger'))
print('ex3 ->',t.log('Called timestamp logger'))
print('ex3 ->',d.log('Called date logger'))

l.log('test1')
t.log('test2')
d.log('test3')