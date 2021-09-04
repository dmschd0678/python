# chapter -4 - 01
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형을 담을 수 있는 자료형[list, tuple, collections, deque])
# 플랫(Flat : 한개의 자료형을 담을 수 있는 자료형[str, bytes, bytearray, array.array, memoryview])
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
