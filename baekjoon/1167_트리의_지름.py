import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V = int(input())
tree = [[] for _ in range(V+1)]
visited = [False]*(V+1)
maxWeight = 0

for _ in range(V):
    tmp_list = list(map(int, input().split()))
    node = tmp_list[0]
    for i in range(1, len(tmp_list)-1, 2):
        tree[node].append((tmp_list[i], tmp_list[i+1]))


def dfs(n, w):
    if visited[n]:
        return
    visited[n] = True
    left, right = 0, 0
    for child, weight in list(tree[n]):
        r = dfs(child, weight)
        if r:  # r의 리턴값이 None이 아닐 때만 거리 계산
            if left <= right:
                left = max(left, r)
            else:
                right = max(right, r)

    global maxWeight
    maxWeight = max(maxWeight, left+right)
    return max(left+w, right+w)


dfs(1, 0)
print(maxWeight)
