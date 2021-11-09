import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)
w_list = []
for i in range(len(arr)):
    weight = arr[i]*(i+1)
    w_list.append(weight)

print(max(w_list))
