import sys
import copy
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
grid_origin = []
for _ in range(N):
    grid_origin.append(list(map(int, sys.stdin.readline().split())))


def dfs(i, j, h):
    if i < 0 or j < 0 or i >= N or j >= N or grid[i][j] <= h:
        return
    grid[i][j] = h
    dfs(i, j+1, h)
    dfs(i, j-1, h)
    dfs(i-1, j, h)
    dfs(i+1, j, h)


h_list = list(set(sum(grid_origin, [])))
if len(h_list) == 1:
    print(1)
else:
    h_list.sort()
    h_max = 0
    for h in h_list:
        grid = copy.deepcopy(grid_origin)
        answer = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > h:
                    answer += 1
                    dfs(i, j, h)
        if answer > h_max:
            h_max = answer

    print(h_max)
