# 분해합 - 브루트포스
import sys
N = int(sys.stdin.readline())

m, _min = N-len(str(N)), N

while True:
    _m_list = list(map(int, [str(m)[i] for i in range(len(str(m)))]))
    if N == m + sum(_m_list) and m < _min:
        _min = m
    elif m < N - 9*len(str(m))+1 or m < 2: # N - 9*(N의 자리수) 이상에서만 생성자 존재
        if _min == N:
            _min = 0
        break
    else:
        m -= 1

print(_min)