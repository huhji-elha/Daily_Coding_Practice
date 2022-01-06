import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N)]
node = list(map(int, input().split()))
node_remove = int(input())
leafNode = 0

for i in range(len(node)):
    if node[i] == -1:
        continue
    tree[node[i]].append(i)

if node_remove == 0:
    print(0)
else:
    queue = deque([0])
    while queue:
        n = queue.popleft()
        if not tree[n]:
            leafNode += 1
        for i in tree[n]:
            if i != node_remove:
                queue.append(i)

    print(leafNode)
