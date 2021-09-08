# Chapter 06 - 01
# 병행성 (concurrency)
# 이터레이터 (Iterator)
# 제네레이터 (Generator)

# 파이썬 반복 가능한 타입
# collections, text, list, Dict, set, Tuple, upacking, *arg... : iterable

# 반복 가능한 이유 -> iter() 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in t:
    print(c)

print()

# while
w = iter(t)

while True:
    try:
        print(next(w))
    except:
        break
print()

# 반복형 확인
from collections import abc

print(dir(t))
print(hasattr(t,'__iter__'))
print(isinstance(t,abc.Iterable))

print()

# next 패턴
class WordSplitter:
    def __init__(self,text):
        self._idx = 0
        self._text = text.split()

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration ^^')
        self._idx += 1
        return word
    def __repr__(self):
        return 'WordSplit(%s)'% (self._text)

wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split()
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return
    def __repr__(self):
        return 'WordSplitGenerator(%s)'% (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)
print(wt,wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))