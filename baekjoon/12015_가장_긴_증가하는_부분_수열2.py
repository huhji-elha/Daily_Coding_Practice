import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Longest Increase Subsequence


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if target <= arr[mid]:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


lis = [arr[0]]
for n in arr[1:]:
    if lis[-1] < n:
        lis += [n]
    elif lis[-1] > n:
        idx = binary_search(lis, n, 0, len(lis))
        lis[idx] = n

print(len(lis))
