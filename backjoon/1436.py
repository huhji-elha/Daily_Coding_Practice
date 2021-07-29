# 브루트포스 - 666
import sys
# import time 
n = int(sys.stdin.readline())
# s = time.time()
_num = 666
i = 1
_666 = 666

while True:
    _num += 1
    if i == n:
        break        
    if "666" in str(_num):
        _666 = _num
        i += 1

# e = time.time()
print(_666)