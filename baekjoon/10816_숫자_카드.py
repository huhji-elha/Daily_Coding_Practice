import sys
from bisect import bisect_left, bisect_right
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
N_arr.sort()

M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))

for m in M_arr:
    res = bisect_right(N_arr, m) - bisect_left(N_arr, m)
    print(res, sep=" ")
