# Chapter 07 - 01
# AsyncIO
# 비동기 I/O Coroutine 작업
# Generator 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# blocking I/O  : 호출된 함수가 자신의 작업을 완료할 때까지 제어권을 가지고 있음, 타 함수는 대기
# Non-Blocking I/O : 호출된 함수(서브 루틴)가 return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# 쓰레드 단점 : 디버깅, 자원 접급 시 레이스컨디션(경쟁상태), 데드락(Dead Lock)-> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요x -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현되어 있어야 하거나, 직접 비동기로 구현해야 됨

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading