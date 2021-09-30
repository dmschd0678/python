"""
Chapter 4
Python Advanced(4) - 나만의 패키지 만들기(3) - PyPi 배포
Keyword - PyPI, build, package deploy
"""

# py_ad_4_3 : 완성된 패키지 import
from py_ad_4_3 import GifConverter as gfc

# 클래스 생성
c = gfc('./project/images/*.png','./project/image_out/result7.gif',(320,420))

# 실행
c.convert_gif()

"""
패키지 배포 순서(PyPI)

1. https://pypi.org 회원가입

"""