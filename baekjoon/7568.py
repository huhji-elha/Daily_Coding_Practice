# 브루트 포스 - 덩치 순위
import sys
n = int(sys.stdin.readline())
_dict = {}
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    _dict[i] = [x, y]

_dict = sorted(_dict.items(), key=lambda x:x[1] ,reverse=True)

for size in _dict:
    r = 1
    for other in _dict:
        if size == other:
            continue
        if size[1][0] < other[1][0] and size[1][1] < other[1][1]:
            r += 1
    size[1].append(r)

_dict.sort()
for d in _dict:
    print(d[1][-1], end=' ')