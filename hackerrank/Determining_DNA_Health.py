"""
https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=false

# 유전자 정보와 헬스 값이 주어졌을때 정해진 범위 내에서 DNA의 헬스 점수 계산하기

6
a b c aa d b
1 2 3 4 5 6
3
1 5 caaab
0 4 xyz
2 4 bcdybc

"""
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
