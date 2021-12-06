import sys
from collections import defaultdict
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = defaultdict(list)
for _ in range(M):
    v1, v2 = list(map(int, sys.stdin.readline().split()))
    arr[v1] += [v2]
    arr[v2] += [v1]

visited = []


def dfs(arr, v, visited):
    visited.append(v)
    for i in arr[v]:
        if i not in visited:
            dfs(arr, i, visited)


dfs(arr, 1, visited)
print(len(visited)-1)
