# Chapter 06 - 5
# Futures 동시성
# 비동기 작업 실행
# 지연시간 (Block) CPU 및 리소스 낭비 방지 -> (file)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능이 향상된다.

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/ 멀티프로세싱 API 통일 -> 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행, 리소스 전체에 락이 걸림, -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython 이용 -> GIL 우회

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [100000,1000000,10000000,100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수
def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait

# as_completed
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()

    # futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExcutor
    # with futures.ThreadPoolExecutor() as excutor:   # with문 객체를 만들고 끝나면 객체 소멸
    with ProcessPoolExecutor()as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator,work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print('Scheduled for {} : {}'.format(work,future))
            print()
        # # wait 결과 출력
        # result = wait(futures_list,timeout = 7)
        #
        # # 성공
        # print('Completed Tasks : '+str(result.done))
        #
        # # 실패
        # print('Pending ones after waiting for 7 seconds : ' + str(result.not_done))
        #
        # # 결과 값
        # print([future.result() for future in result.done])


        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result,done))
            print('Future Cancelled : {}'.format(cancelled))
    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\nTime : {:.2f}s'

    # 최종결과 출력
    print(msg.format(end_tm))

# 실행
if __name__ == '__main__':
    main()
