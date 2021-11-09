import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))
start = 0
answer = 0
for s, e in arr:
    if s >= start:
        answer += 1
        start = e
print(answer)
