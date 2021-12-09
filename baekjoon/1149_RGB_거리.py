import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

"""
RGB 점화식
Red: Cost[n][0] = min(Cost[n-1][1], Cost[n-1][2]) + Cost[n][0]
Green: Cost[n][1] = min(Cost[n-1][0], Cost[n-1][2]) + Cost[n][1]
Blue: Cost[n][2] = min(Cost[n-1][0], Cost[n-1][1]) + Cost[n][2]

"""

dp = [[0]*3 for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]


def rgb(n, color):
    if not dp[n][color]:
        if color == 0:
            dp[n][color] = min(rgb(n-1, 1), rgb(n-1, 2)) + cost[n][color]
        elif color == 1:
            dp[n][color] = min(rgb(n-1, 0), rgb(n-1, 2)) + cost[n][color]
        else:
            dp[n][color] = min(rgb(n-1, 0), rgb(n-1, 1)) + cost[n][color]
    return dp[n][color]


print(min([rgb(N-1, 0), rgb(N-1, 1), rgb(N-1, 2)]))
