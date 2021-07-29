# 수 정렬하기 3 - 메모리 8MB
    
import sys

n = int(sys.stdin.readline())
count_arr = [0]*10001

for _ in range(n):
    count_arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count_arr[i] != 0:
        # sys.stdout.write(str(a)+"\n") --> 이 방법은 메모리 초과가 됨.
        for _ in count_arr[i]:
            print(i)