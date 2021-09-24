"""
Chapter 1
Python Advanced(1) - Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception
"""
"""
컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정화한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)
"""

# ex1
file = open('textfile.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()

# ex2

with open('textfile2.txt', 'w') as f:
    f.write('Context Manager Test1\nContextlib Test2.') # 알아서 자원 반환

# ex3
# use Class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name,method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print("Logging exceprion {}".format((exc_type,value,trace_back)))
        self.file_obj.close()

with MyFileWriter('textfile3.txt', 'w') as f:
    f.write('Context Manager Test1\nContextlib Test3.')