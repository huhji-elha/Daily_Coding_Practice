import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    n = int(input().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))
