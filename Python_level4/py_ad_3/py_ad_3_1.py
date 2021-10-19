"""
Section 3
Concurrency, CPU Bound, I/O Bound - What is Concurrency
Keyword - Concurrency
"""
"""
Concurrency(동시성)

- CPU 가용성 극대화를 위해 Paralleism의 단점 및 어려움을 소프트웨어(구현)레벨에서 해결하기 위한 방법
- 싱글코어에 멀티스레드 패턴으로 작업을 처리
- 동시 작업에 있어 일정량 처리 후 다음 작업으로 넘기는 방식
- 즉, 제어권을 주고 받으며 작업 처리 패턴, 병렬적과 다르지만 유사한 처리 방식

Concurrency(동시성) vs Parralleism(병렬성)

동시성 : 논리적, 동시 실행 패턴(논리적), 싱글 코어, 멀티 코어 실행 가능, 한 개의 작업 공유 처리, 디버깅 매우 어려움, Mutex, DeadLock
병렬성 : 물리적, 물리적으로 동시 실행, 멀티 코어에서 구현 가능, 주로 별개의 작업, 디버깅 어려움, OpenMP, MPI, CUDA

"""