import sys
N = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, s, e):
    if s > e:
        return None
    mid = (s+e)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, s, mid-1)
    else:
        return binary_search(arr, target, mid+1, e)


n_arr.sort()
for m in m_arr:
    s = 0
    e = len(n_arr)-1
    res = binary_search(n_arr, m, s, e)
    if res is not None:
        print(1)
    else:
        print(0)
