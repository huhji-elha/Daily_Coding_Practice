import sys
R, C = list(map(int, sys.stdin.readline().split()))
alpha_grid = []
for _ in range(R):
    alpha_grid.append(list(sys.stdin.readline())[:-1])

alpha_set = set()
tmp = []


def dfs(i, j):
    if i < 0 or j < 0 or i >= R or j >= C or alpha_grid[i][j] in alpha_set:
        return
    alpha_set.add(alpha_grid[i][j])
    dfs(i, j+1)
    dfs(i, j-1)
    dfs(i-1, j)
    dfs(i+1, j)


dfs(0, 0)
print(alpha_set)
