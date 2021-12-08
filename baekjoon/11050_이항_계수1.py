import sys
N, K = list(map(int, sys.stdin.readline().split()))

# 팩토리얼로 구하기


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(N)//factorial(K)//factorial(N-K))

# 다이나믹 프로그래밍으로 풀기

dp_list = [[0]*(K+1) for _ in range(N+1)]


def dp(n, k):
    if dp_list[n][k] > 0:
        return dp_list[n][k]

    if n == k or k == 0:
        dp_list[n][k] = 1
        return dp_list[n][k]

    dp_list[n][k] = dp(n-1, k-1) + dp(n-1, k)
    return dp_list[n][k]


print(dp(N, K))
