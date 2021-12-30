import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
tomato = [sys.stdin.readline().split() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

queue = deque([])
for i in range(N):
    for j in range(M):
        if tomato[i][j] == "1":
            queue.append((i, j))
            visited[i][j] = 1
        elif tomato[i][j] == "-1":
            visited[i][j] = -1

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
res = 0
while queue:
    x, y = queue.popleft()
    res = max(res, visited[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and tomato[nx][ny] == "0":
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

v = set(sum(visited, []))
if 0 in v:
    print(-1)
else:
    print(res-1)
