"""
Section 2
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPoolExecutor
Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URL
URLS = [
    'https://www.daum.net/',
    'https://www.cnn.com/',
    'http://naver.com/',
    'https://google.com/',
    'https://some-made-up-domain.com/'
]

# 실행 함수
def load_url(url, timeout):
    with urllib.request.urlopen(url,timeout = timeout) as conn:
        # print(conn.read())
        return conn.read()

def main():
    # 프로세스 풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        #Future 로드(실행 X)
        future_to_url = {executor.submit(load_url,url, 10) : url for url in URLS}

        # 중간 확인
        # print(future_to_url)

        # 실행
        for future in as_completed(future_to_url):  # timeout = 1
            # Key 값이 Future 객체
            url = future_to_url[future] # future_to_url.get()

            try:
                # 결과
                data = future.result()
            except Exception as e:
                # 예외 처리
                print('%r generated an exception : %s' % (url,e))
            else:
                # 결과 확인
                print('%r page is %d bytes' % (url,len(data)))
# 메인시작
if __name__ == '__main__':
    main()