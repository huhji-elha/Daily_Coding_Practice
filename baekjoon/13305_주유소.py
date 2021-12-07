import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

buy = 0
cheaper_idx = 0
for i in range(N-1):
    if price[i] < price[cheaper_idx]:
        cheaper_idx = i
    buy += price[cheaper_idx]*road[i]

print(buy)
