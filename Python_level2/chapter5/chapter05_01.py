# Chapter 05 - 01
# 일급 함수 (일급 객체)

# 파이썬 함수 특징

# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능 (return)

# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''

    if n == 1:
        return 1
    return n * factorial(n - 1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial)))- set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print('\n')

# 변수 할당

var_function = factorial
print(var_function)
print(var_function(10))
print(list(map(var_function,range(1,11))))

# 함수 인수 전달, 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

print(list(map(var_function, filter(lambda x: x % 2, range(1,6)))))
print([var_function(i) for i in range(1,6) if i % 2])

print()

# reduce+*
from functools import reduce
from operator import add

print("reduce",reduce(add, range(1,11)))

print("sum",sum(range(1,11)))

# 익명 함수 (lambda)
# 가급적 주석 작성!
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 작성

print("lambda",reduce(lambda x,t : x + t, range(1,11)))

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한 지 확인
# 호출 가능 확인

# 3.14는 함수가 아니라서 false가 나옴
print(callable(str), callable(list), callable(var_function), callable(factorial), callable(3.14))

print()

# partial 사용법 : 인수 고정 -> call-back 함수 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul,5)   # 함수를 인자로 전달 가능, 함수를 변수에 할당

# 고정 추가
six = partial(five, 6)
print(five(10))
print(six())

print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))