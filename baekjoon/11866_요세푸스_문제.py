import sys
from collections import deque
N, K = list(map(int, sys.stdin.readline().split()))
que = deque([i for i in range(1, N+1)])
res = []

while len(res) < N:
    for i in range(K):
        if i == K-1:
            res.append(que.popleft())
        else:
            n = que.popleft()
            que.append(n)

print("<", end='')
for i in range(N):
    if i == N-1:
        print(res[i], end='')
    else:
        print(str(res[i])+", ", end='')
print(">")
