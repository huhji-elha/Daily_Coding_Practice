import sys
sys.setrecursionlimit(10000)
while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))

    def dfs(i, j):
        if i < 0 or j < 0 or i >= h or j >= w or arr[i][j] == 0:
            return
        arr[i][j] = 0
        dfs(i, j+1)  # 동
        dfs(i, j-1)  # 서
        dfs(i-1, j)  # 남
        dfs(i+1, j)  # 북
        dfs(i-1, j+1)  # 오른쪽 대각선 위
        dfs(i+1, j+1)  # 오른쪽 대각선 아래
        dfs(i-1, j-1)  # 왼쪽 대각선 위
        dfs(i+1, j-1)  # 왼쪽 대각선 아래

    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                answer += 1
                dfs(i, j)

    print(answer)
