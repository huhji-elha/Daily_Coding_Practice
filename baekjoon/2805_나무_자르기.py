# pypy로 실행하기

import sys
N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
s = 0
e = max(arr)
while s <= e:
    mid = (s+e)//2
    length = 0
    for x in arr:
        if x > mid:
            length += x - mid  # 여기서 sum함수 쓰기! sum이 내장함수라서 c로 구현되어있기 때문에 더 빠르다.
    if length < M:
        e = mid-1
    else:
        result = mid
        s = mid+1

print(result)
