import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# def binary_search(lis_arr, start, end, target):
#     while start <= end:
#         mid = (start+end)//2
#         if target <= lis_arr[mid]:
#             res = mid
#             end = mid - 1
#         else:
#             start = mid + 1
#     return res


idx_arr = [(0, arr[0])]
lis_arr = [arr[0]]
for a in arr[1:]:
    if lis_arr[-1] < a:
        lis_arr.append(a)
        idx_arr.append((len(lis_arr)-1, a))
    else:
        idx = bisect_left(lis_arr, a)
        idx_arr.append((idx, a))
        lis_arr[idx] = a

idx_arr.reverse()

n = len(lis_arr)-1
res = []
for i in range(N):
    if idx_arr[i][0] == n:
        res.append(idx_arr[i][1])
        n -= 1

print(len(lis_arr))
print(*res[::-1])
