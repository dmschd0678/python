# Chapter 06 - 4
# Futures 동시성
# 비동기 작업 실행
# 지연시간 (Block) CPU 및 리소스 낭비 방지 -> (file)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다.

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/ 멀티프로세싱 API 통일 -> 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법 1
# concurrent.futures 사용법 2

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행, 리소스 전체에 락이 걸림, -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython 이용 -> GIL 우회

import os
import time
from concurrent import futures

WORK_LIST = [10000,100000,1000000,10000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수
def sum_generator(n):
    return sum(n for n in range(1, n+1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExcutor
    # with futures.ThreadPoolExecutor() as excutor:   # with문 객체를 만들고 끝나면 객체 소멸
    with futures.ProcessPoolExecutor()as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\nResult -> {} Time : {:.2f}s'

    # 최종결과 출력
    print(msg.format(list(result),end_tm))

# 실행
if __name__ == '__main__':
    main()
