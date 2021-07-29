# 정렬 - 좌표 정렬하기 2
import sys 
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:(x[1],x[0]))
for l in arr:
    print(' '.join(map(str, l)))