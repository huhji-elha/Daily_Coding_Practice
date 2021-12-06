import sys
from bisect import bisect_left
N, C = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start = 0
end = len(arr)

c = C - 2
while start <= end:
    mid = (start+end)//2
    v = arr[mid]-arr[start]
    if end - mid > c - 1:
        search = arr[mid]+v
        for _ in range(c - 1):
            if mid + bisect_left(arr[mid:], search) < end:
                print(search)
                search += v
            else:
                v = None
                break
    if not v:
        end = mid - 1
    else:
        end = mid - 1
