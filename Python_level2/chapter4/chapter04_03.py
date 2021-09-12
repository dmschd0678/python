# chapter 04 - 03
# 시퀀스형

# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한 개의 자료형을 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview])

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시 테이블
# Key에 Value를 저장하는 구조
# ex) 파이썬 dict
# 키 값의 연산 결과에 따라 직접 접근이 가능
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Dict
#print(__builtins__.__dict__)

# Hach 값 확인

t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print(hash(t1))
# print(hash(t2)) # 예외 list 때문에

print()

# Dict setdefault

source = (('k1','val1'),
          ('k1','val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k,v in source:
    new_dict2.setdefault(k,[]).append(v)

print(new_dict2)

# 주의

new_dict3 = {k : v for k,v in source}

print(new_dict3)