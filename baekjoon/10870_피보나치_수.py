# 다이나믹 프로그래밍으로 풀기
import sys
N = int(sys.stdin.readline())

# 탑 다운 방식
d = [0]*(N+1)
d[0] = 0


def fibo(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(N))


# 바텀업 방식
d = [0]*(N+1)
d[0] = 0
d[1] = 1
d[2] = 1

for i in range(3, N+1):
    d[i] = d[i-1]+d[i-2]

print(d[N])
