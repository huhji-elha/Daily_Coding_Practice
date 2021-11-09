import sys
N, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

answer = 0
arr = arr[::-1]
for n in arr:
    answer += K//n
    K = K % n

print(answer)
