"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=false

1에서 100까지 중 하나의 수가 주어졌을 때 팩토리얼 구하기
"""
# python은 int 범위를 초과하는 수를 계산할 때는 자동으로 long으로 변환된다.
# 아이디어01 : math 라이브러리의 factorial 사용하기
from functools import reduce
import math


def extraLongFactorials01(n):
    return math.factorial(n)


# 아이디어02 : 단순 반복문
def extraLongFactorials02(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer

# 아이디어03 : 재귀함수


def extraLongFactorials03(n):
    return n * extraLongFactorials03(n-1) if n > 1 else 1


# 아이디어04 : 함수형 프로그래밍 방식인 reduce를 사용하기
# map, filter, reduce는 함수형 프로그래밍 방식인 파이썬 기능이다.

def extraLongFactorials04(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

# 아이디어05 : 메타 프로그래밍 방식을 사용하기
# 메타 프로그래밍이란 컴퓨터가 프로그램을 읽어 생성, 분석, 실행할 수 있는 것을 말한다.
# 간단한 예시로 입력 문자열을 이름으로 갖는 함수를 생성할 수 있다.
# 파이썬의 eval 기능을 사용한다.


def extraLongFactorials05(n):
    if not n:
        return 1
    return eval('*'.join([str(i) for i in range(1, n+1)]))
