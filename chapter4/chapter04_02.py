# chapter -4 - 02
# 시퀀스형

# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한 개의 자료형을 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview])

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)


# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

print(divmod(100,9))
print(divmod(*(100,9)))
print(*(divmod(100,9)))


print()

x, y, *rest = range(10)
print(x,y,rest)

x,y, *rest = range(2)
print(x,y,rest)

x, y, *rest = 1,2,3,4,5
print(x,y,rest)

print()

# Mutable(가변), Imutable(불변)

l = (15,20,25)
m = [10,20,25]

print(l, id(l))
print(m,id(m))

l = l * 2
m = m * 2

print(l,id(l))
print(m,id(m))


l *= 2
m *= 2

# 리스트는 위에 연산 후에도 id가 같다
# 튜플은 id 재할당
print(l,id(l))
print(m,id(m))

# sort, sorted
# reverse, key = len, key, str.lower, key = func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ["orange", "apple", "mango", "papaya","lemon","strawbetty", "coconut"]

print("sorted : ",sorted(f_list))
print("sorted reverse :", sorted(f_list, reverse= True))
print("sorted key = len:", sorted(f_list, key=len))
print("sorted key = lamda:", sorted(f_list, key= lambda  x: x[-1]))
print("sorted key = lamda, reverse :", sorted(f_list, key= lambda  x: x[-1], reverse= True))

print(f_list)


# sort   : 정렬 후 객체 직접 변환
# 반환값 : None
print('sort : ',f_list.sort(), f_list)
print('sort : ', f_list.sort(reverse=True), f_list)
print('sort : ', f_list.sort(key = len), f_list)
print('sort : ', f_list.sort(key = lambda x : x[-1]), f_list)
print('sort : ', f_list.sort(key = lambda x : x[-1], reverse= True), f_list)

# List, Array 사용법
# 리스트 : 융통성 , 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 호환)

