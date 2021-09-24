"""
Chapter 2
Python Advanced(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__
"""
"""
가장 대표적인 with 문 이해
Contextlib 데코레이터 사용
코드 직관적, 예외 처리 용이성
"""

import contextlib
import time

# ex1
# Use decorator

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f # __enter__
    f.close() # __exit__

with my_file_writer("my_file.txt",'w') as f:
    f.write('Context Manager Test\nContextlib Test')

# ex2
# Use decorator

@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try:    # __enter__
        yield start
    except Exception as e:
        print('Logging exception : {} : {}'.format(msg,e))
        raise
    else:
        print('{}: {}s'.format(msg,time.monotonic() - start))

with ExcuteTimerDc('Start job!')as v:
    print('Received start monotonic2 : {}'.format(v))
    # Excute job
    for i in range(10000000):
        pass
    # 예외 만들기
    # raise ValueError('occurred')