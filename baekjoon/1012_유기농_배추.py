import sys
sys.setrecursionlimit(10000)
T = int(sys.stdin.readline())


def dfs(i, j):
    if i < 0 or j < 0 or i >= N or j >= M or grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(i, j+1)  # 동
    dfs(i, j-1)  # 서
    dfs(i+1, j)  # 남
    dfs(i-1, j)  # 북


for _ in range(T):
    M, N, K = list(map(int, sys.stdin.readline().split()))
    grid = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = list(map(int, sys.stdin.readline().split()))
        grid[y][x] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                answer += 1
                dfs(i, j)
    print(answer)
