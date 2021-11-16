import sys
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))
N_arr.sort()
print(N_arr)
print(M_arr)


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


for m in M_arr:
    res = binary_search(N_arr, m, 0, len(N_arr)-1)
    if res is not None:
        print(1, sep=" ")
    else:
        print(0, sep=" ")
