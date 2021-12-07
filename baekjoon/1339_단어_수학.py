import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip())[::-1])

math_order = defaultdict(int)
for l in arr:
    v = 1
    for i in l:
        math_order[i] += v
        v *= 10

math_order = sorted(math_order.items(), key=lambda x: x[1], reverse=True)
res = 0
score = 9
for k, v in math_order:
    res += v*score
    score -= 1

print(res)
