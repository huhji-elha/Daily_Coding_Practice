# 정렬 - 좌표 압축
import sys
import copy 
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

_arr = list(set(copy.deepcopy(arr)))
_arr.sort()
_dict = {}
for i, n in enumerate(_arr):
    _dict[n] = i

for a in arr:
    print(_dict[a], end=' ')

# 더 좋은 방법 : 
# keys = sorted(set(arr))
# location = dict(zip(keys, map(str, range(len(keys)))))
