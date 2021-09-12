# Chapter 06 - 3
# 병행성 (concurrency) : 한 컴퓨터가 여러 일을 동시에 수행   -> 단일 프로그램안에서 여러 일을 쉽게 해결
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 일을 동시에 수행  -> 속도 ↑
# 코루틴 (Coroutine)

# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : os가 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행
# 코루틴 : 루틴 실행 중 중지를 해도 -> 기억을 함 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드, 멀티쓰레드 -> 복잡 -> 공유되는 자원이 있어 -> 교착 상태가 일어날 수 도 있다, 컨텍스트 스위칭 비용이 크다, 자원을 소비할 가능성이 증가
# def -> async, yeild -> await

# 코루틴 Ex1

# async coroutine1():
def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine receved : {}'.format(i))

# 코루틴은 제네레이터에서 파생됨

# 메인 루틴
#제네레이터 선언

cr1 = coroutine1()

print(cr1, type(cr1)) # 제네레이터 타입

# yield 지점까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 : None
# 값 전송
# cr1.send(100)   # send : next의 기능도 포함

# 잘못된 사용
cr2 = coroutine1()
# cr2.send(100)

# 코루틴 Ex2

# GEN_CREATED : 처음 대기 상태
# GEN_RUUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료

# await coroutine2():
def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    # y는 받고 x는 보내는 것, 양방향으로 데이터를 주고 받는다
    y = yield x
    print('>>> coroutin received : {}'.format(y))
    z = yield x + y
    print('>>> coroutin received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))   # 현재 상태 : GEN_CREATED

print(next(cr3))

print(getgeneratorstate(cr3))   # 현재 상태 : GEN_SUSPENDED

print(cr3.send(100))   # y에 100을 보냄 x + y를 받아온다

print()

# 코루틴 Ex3
# stopIteration 자동처리(Python 3.5 -> await)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1)) # A
print(next(t1)) # B
print(next(t1)) # 1
print(next(t1)) # 2
print(next(t1)) # 3
# print(next(t1)) # stopiteration

t2 = generator1()

print(list(t2)) # ['A', 'B', 1, 2, 3]

print()

# generator1과 결과가 똑같다
def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3)) stopiteration