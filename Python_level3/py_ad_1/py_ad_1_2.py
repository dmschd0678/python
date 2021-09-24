"""
Chapter1 Advanced (1) - Lambda, Reduce, Map, Filter Function
Keyword - lambda, map, filter, reduce
"""
"""
lambda 장점 : 익명, 힙 영역, 사용 즉시 소멸, pythonic, 파이썬 가비지 컬렉션(Count = 0)
일반 함수 : 재사용성을 위해 메모리에 저장
시퀀스형 전처리에 Reduce, Map, Filter를 주로 사용
"""

# ex1   lambda
cul = lambda a,b,c : a + b + c

print('ex1 ->',cul(10,15,20))

# ex2   map
digits1 = [x * 10 for x in range(1,11)]
print('ex2 ->',digits1)

def ex2_func(x):
    return x ** 2

result = list(map(lambda i: i ** 2, digits1)) # map(함수, list)
print('ex2 ->',result)

def also_square(num):
    def double(x):
        return x ** 2
    return map(double,num)

print('ex2 ->',list(also_square(digits1)))

# ex3   filter
digits2 = [i for i in range(1,11)]

result = list(filter(lambda x: x % 2 == 0, digits2))    # filter(함수, list)
print('ex3 ->',result)

def also_even(num):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even,num)
print('ex3 ->',list(also_even(digits2)))

# ex4   reduce
from functools import reduce

digits3 = [i for i in range(1, 101)]

result = reduce(lambda x, y: x + y, digits3)    # 반환값 list X 누적된 계산 값
print('ex3 ->',result)

def also_add(num):
    def add_plus(x,y):
        return x + y
    return reduce(add_plus,num)

print("ex4 ->",also_add(digits3))

