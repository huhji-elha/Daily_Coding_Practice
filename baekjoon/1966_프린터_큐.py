import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    printer = list(map(int, input().split()))

    que = deque([(i, printer[i]) for i in range(N)])
    printer.sort()
    res = 0

    while que:
        if que[0][1] == printer[-1]:
            n = que.popleft()
            printer.pop()
            res += 1
            if n[0] == M:
                break
        else:
            que.rotate(-1)
    print(res)
