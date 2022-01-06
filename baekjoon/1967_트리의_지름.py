import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
maxWeight = 0

for _ in range(N-1):
    root, child, weight = map(int, input().split())
    tree[root].append((child, weight))


def dfs(n, w):
    left, right = 0, 0
    for child, weight in tree[n]:
        r = dfs(child, weight)
        if left <= right:
            left = max(left, r)
        else:
            right = max(right, r)
    global maxWeight
    maxWeight = max(maxWeight, left+right)
    return max(left+w, right+w)


dfs(1, 0)
print(maxWeight)
