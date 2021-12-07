import sys
N = sys.stdin.readline()  # 120
arr = list(map(int, N.rstrip()))  # [1, 2, 0]
arr.sort(reverse=True)  # [2, 1, 0]

if 0 not in arr:
    print(-1)
elif sum(arr) % 3 != 0:
    print(-1)
else:
    res = ''.join(list(map(str, arr)))
    print(int(res))
