"""
Section 1
Multithreading - Thread(5) - prod vs Cons using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)
"""
"""
Producer-Consumer Pattern
(1) 멀티스레드 디자인 패턴의 정석
(2) 서버 측 프로그래밍의 핵심
(3) 주로 허리역할, 중요

Python Event 객체
(1) Flaf 초기 값(0)
(2) set() -> 1, Clear() -> 0, wait(1 -> return, 0-> 대기), isSet() -> 현 플래그 상태

"""

import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    """
    네트워크 대기 상태라 가정(서버)
    """
    while not event.is_set():
        message = random.randint(1,11)
        logging.info("Producer got message : %s",message)
        queue.put(message)
    logging.info("Producer recived event Exiting")

# 소비자
def consumer(queue, event):
    """
    응답 받고 소비하는 것으로 가정 or DB 저장
    """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message : %s (size %d)",message,queue.qsize()
        )
    logging.info("Consumer sending event Exiting")

if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # with Context
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as excutor:
        excutor.submit(producer,pipeline,event)
        excutor.submit(consumer,pipeline,event)

        # 실행 시간 조정
        time.sleep(2)

        logging.info("Main : about to set event")

        # 프로그램 종료
        event.set()