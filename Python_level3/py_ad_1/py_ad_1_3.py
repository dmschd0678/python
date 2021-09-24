"""
Chapter 1
Python Advanced(1) - Shallow Copy & Deep copy
Keyword - shallow & deep copy
"""
"""
객체 복사 종류 : Copy, Shallow Copy, Deep Copy
정확한 이해 후 사용 -> 프로그래밍 개발 중요(문제 발생 요소)
가변 : list, set, dict
"""

# ex1 - Copy
# Call by value, Call by Reffernce Call by Share
a_list = [1,2,3,[4,5,6],[7,8,9]]
b_list = a_list # Call by Refference

print("ex1 ->",id(a_list))
print("ex1 ->",id(b_list))  # 같은 id값을 참조하고 있다

b_list[2] = 100

print("ex1 ->",a_list)
print("ex1 ->",b_list)

b_list[3][2] = 100

print("ex1 ->",a_list)
print("ex1 ->",b_list)

# immutable : int, str, float, bool, unicode ...

# ex2 - Shallow Copy
import copy

c_list = [1,2,3,[4,5,6],[7,8,9]]
d_list = copy.copy(c_list)

print('ex2 ->',id(c_list))
print('ex2 ->',id(d_list))

d_list[1] = 100

print('ex2 ->',c_list)
print('ex2 ->',d_list)

d_list[3].append(1000)
d_list[4][1] = 10000

print('ex2 ->',c_list)  # c_list와 d_list의 id 값은 다르나 내부의 객체 id는 같다
print('ex2 ->',d_list)

# ex3 - Deep Copy
e_list = [1,2,3,[4,5,6],[7,8,9]]
f_list = copy.deepcopy(e_list)

print('ex3 ->',id(e_list))
print('ex3 ->',id(f_list))

f_list[3].append(1000)
f_list[4][1] = 10000

print('ex3 ->',e_list)
print('ex3 ->',f_list)  # deep copy는 내부의 객체의 id값도 다르다