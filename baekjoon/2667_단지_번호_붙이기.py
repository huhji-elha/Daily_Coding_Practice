import sys
N = int(sys.stdin.readline())
grid = []
for _ in range(N):
    grid.append(list(sys.stdin.readline())[:-1])


def dfs(i, j):
    global count
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
        return
    grid[i][j] = "0"
    count += 1
    dfs(i, j+1)  # 동
    dfs(i, j-1)  # 서
    dfs(i+1, j)  # 남
    dfs(i-1, j)  # 북


count_list = []
answer = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            count = 0
            answer += 1
            dfs(i, j)
            count_list.append(count)
count_list.sort()
print(answer)
print(*count_list, sep='\n')
