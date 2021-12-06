import sys
from collections import deque, defaultdict
N, M, V = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    v1, v2 = list(map(int, sys.stdin.readline().split()))
    graph[v1] += [v2]
    graph[v2] += [v1]


def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')
    for i in sorted(graph[x]):
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)


dfs(graph, V, [False]*20000)
print()
bfs(graph, V, [False]*20000)
