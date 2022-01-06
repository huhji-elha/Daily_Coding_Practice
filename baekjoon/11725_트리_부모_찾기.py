from collections import deque
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

root_node = [-1]*(N+1)

# # dfs
# def dfs(n):
#     for i in tree[n]:
#         if root_node[i] == -1:
#             root_node[i] = n
#             dfs(i)


# dfs(1)
# for i in root_node[2:]:
#     print(i)

# bfs
queue = deque([1])
while queue:
    node = queue.popleft()
    for i in tree[node]:
        if root_node[i] == -1:
            root_node[i] = node
            queue.append(i)

for i in root_node[2:]:
    print(i)
