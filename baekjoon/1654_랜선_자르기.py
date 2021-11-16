# "N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다."

import sys
K, N = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)
res = 0
answer = 0
while start <= end:
    mid = (start+end)//2
    res = 0
    for l in arr:
        if l >= mid:
            res += l//mid
    if res < N:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)
