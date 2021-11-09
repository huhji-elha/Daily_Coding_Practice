import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 0
n = 0
for a in arr:
    n += a
    answer += n

print(answer)
