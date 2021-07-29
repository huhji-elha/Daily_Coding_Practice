# 정렬 - 통계학
import sys
from collections import Counter 
import time 

n = int(sys.stdin.readline())

_arr = [int(sys.stdin.readline()) for _ in range(n)]
# s = time.time()
_arr.sort()
# 1. 산술평균
print(round(sum(_arr)/len(_arr)))

# 2. 중앙값    
print(_arr[len(_arr)//2])

# 3. 최빈값
c = dict(Counter(_arr))
_max_list = []
_max = max(c.values())
for k,v in c.items():
    if _max == v:
        _max_list.append((k, v))

if len(_max_list) > 1:
    print(_max_list[1][0])
else:
    print(_max_list[0][0])
    
# 4. 범위
print(_arr[-1] - _arr[0])

# e = time.time()
# print(e-s)