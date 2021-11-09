import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A_sorted = [0]*N
B_sorted = sorted([(B[i], i) for i in range(N)], reverse=True)
a_arr = sorted(A)

for i in range(N):
    A_sorted[B_sorted[i][1]] = a_arr[i]

answer = sum([a*b for a, b in zip(A_sorted, B)])
print(answer)
