# 정렬 - 내림차순
import sys
arr = list(map(int, sys.stdin.readline().rstrip()))
arr.sort(reverse=True)
print(''.join(map(str,arr)))
