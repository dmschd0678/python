# Chapter 05 - 03
# 일급 함수 (일급 객체)

# 클로저 기초
# 클로저 : 외부에서 호출된 함수의 변수 값, 상태(레퍼런스) 복사 후 저장 -> 접근(액세스) 가능

# Closure 사용

def closure_ex1():
    # Free variable 자유 변수
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series,len(series)))
        return sum(series) / len(series)
    return averager # chapter 5 - 1 함수 결과 반환



avg_closure1 = closure_ex1()
print(avg_closure1) # 함수가 리턴되어 있음
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__)) # co~ 함수
print()
print(avg_closure1.__code__.co_freevars) # 자유 변수 출력
print()
print(avg_closure1.__closure__[0].cell_contents)

print('\n')

# 잘못된 클로저 사용
def closure_ex2():
    #Free varialble
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) 예외 발생

def closure_ex3():
    #Free varialble
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt,total  # 자유변수 선언
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))