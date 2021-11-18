import sys
N, C = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
if C == 2:
    answer = arr[-1] - arr[0]
# else:
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         mid = (start+end)//2
#         if (len(arr)-1) - mid < C-2:
#             break
#         if (arr[mid] - arr[0]) > (arr[-1] - arr[mid])*(C-2):
