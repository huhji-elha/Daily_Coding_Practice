# 수 정렬하기
import sys
n = int(sys.stdin.readline())
_arr = []
for i in range(n):
    _arr.append(int(sys.stdin.readline()))
    
_arr.sort()
for a in _arr:
    print(a)