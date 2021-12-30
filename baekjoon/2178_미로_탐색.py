import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([(0, 0)])
visited[0][0] = 1

# BFS 방식으로 풀기 - 경로 count를 visited에 표시한다!
while queue:
    x, y = queue.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == "1":
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
