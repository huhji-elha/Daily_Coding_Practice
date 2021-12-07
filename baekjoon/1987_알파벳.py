import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
R, C = map(int, input().split())
alpha_grid = [list(map(lambda x: ord(x) - 65, input().rstrip()))
              for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
alpha = [0]*26


def dfs(x, y, count):
    global res_max
    res_max = max(res_max, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and alpha[alpha_grid[nx][ny]] == 0:
            alpha[alpha_grid[nx][ny]] = 1
            dfs(nx, ny, count+1)
            alpha[alpha_grid[nx][ny]] = 0


res_max = 1
alpha[alpha_grid[0][0]] = 1
dfs(0, 0, 1)
print(res_max)
