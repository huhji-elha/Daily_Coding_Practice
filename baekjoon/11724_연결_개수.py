import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

N, M = list(map(int, sys.stdin.readline().split()))
arr = defaultdict(list)
for _ in range(M):
    v1, v2 = list(map(int, sys.stdin.readline().split()))
    arr[v1] += [v2]
    arr[v2] += [v1]

visited = [False]*1001


def dfs(arr, v, visited):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(arr, i, visited)


answer = 0
for v in arr.keys():
    if not visited[v]:
        answer += 1
        dfs(arr, v, visited)

print(answer + (N - len(arr.keys())))
