"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword = scope, global, nonlocal, locals, globals
"""

"""
전역변수는 주로 변하지 않는 고정 값에 사용한다
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
전역변수를 지역내에서 수정하는 것은 권장 X
"""

# ex1
a = 10  # global variable

def foo():
    # Read global variable
    print("ex1 ->",a)

foo()

# Read global variable
print("ex1 ->",a)

# ex 2
b = 20

def bar():
    b = 30  # Local variable
    print("ex2 ->",b)    # Read Local variable

bar()
print("ex2 ->",b)    # Read global variable

# ex3

c = 40

def foobar():
    # c = c + 10    # UnboundLocalError
    # c = 10
    # c += 10
    print("ex3 ->",c)

foobar()

# ex4

d = 50

def barfoo():
    global d
    d = 60
    d += 100
    print("ex4 ->",d)
barfoo()

print("ex4 ->",d)

# ex5 (중요)  # 클로저 형식
def outer():
    e = 70
    def inner():
        nonlocal e  # 변수 값 유지
        e += 10
        print("ex5 ->",e)
    return inner

in_test = outer()

in_test()
in_test()

# ex6   locals
def func(var):
    x = 10
    def printer():
        print("ex6 >","Printer Func Inner")
    print("Func Inner",locals())    # 지역 전체 출력

func('Hi')

# ex7
print("ex7 ->", globals())  # 전역 전체 출력
globals()['test_variable'] = 100
print("ex7 ->",globals())

# ex8 (지역 -> 변역 변수 생성)
for i in range(1,10):
    for k in range(1,10):
        globals()['plus_{}_{}'.format(i,k,)] = i + k    # 변수 만들기

print(globals())
print("ex8 ->", plus_5_5)
print("ex8 ->", plus_9_9)