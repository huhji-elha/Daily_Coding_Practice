import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

arr.sort()
start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2
    budget_sum = 0
    for i in range(len(arr)):
        if arr[i] < mid:
            budget_sum += arr[i]
        else:
            budget_sum += (len(arr)-i)*mid
            break
    if budget_sum <= M:  # 정확하게 일치할 때도 정답에 포함
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
