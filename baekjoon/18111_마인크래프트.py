import sys
from collections import Counter
input = sys.stdin.readline
N, M, B = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr += list(map(int, input().split()))

_sum = sum(arr)
arr = dict(Counter(arr))


def get_height(height):
    t = 0
    for h in arr:
        if h > height:
            t += (h - height)*2*arr[h]
        elif h < height:
            t += (height - h)*arr[h]
    return t


_len = N*M
res = float("inf")
res_height = -1
for i in range(257):
    if _sum + B >= i*_len:
        ans = get_height(i)
        if ans <= res:
            res = ans
            res_height = i

print(res, res_height)
