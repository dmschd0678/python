# chapter 04 - 01
# 시퀀스형

# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한 개의 자료형을 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview])

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)


# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending lists)
chars = "+_)(*&^%$#@!)"
code_list1 = []
#code_list1 = [i for i in chars]

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

#Comprehending lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

#Comprehending lists + Map, Filter

code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
import array

tuple_g = (ord(s) for s in chars)

print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

array_g = array.array('I', (ord(s) for s in chars))

print(array_g)
print(type(array_g))
print(array_g.tolist())

print()

# 제네레이터 예제

print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)

print()

# -------------리스트 주의---------------

mark1 = [['~'] * 3 for _ in range(4)]
mark2 = [['~'] * 3 ] * 4

print(mark1)
print(mark2)

print()

# 수정

mark1[0][1] = 'x'
mark2[0][1] = 'x'

# mark1 은 ID 값 다름, mark2 는 ID값이 같아 모두 변경됨
print(mark1)    #[['~', 'x', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(mark2)    #[['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~']]

# 증명
print([id(i) for i in mark1])   # id 값 모두 다름
print([id(i) for i in mark2])   # id 값 모두 같음

