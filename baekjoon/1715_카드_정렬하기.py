from queue import PriorityQueue
import heapq
import sys
input = sys.stdin.readline
N = int(input())

# PriorityQueue로 풀기 (1032ms)
n_queue = PriorityQueue()
for _ in range(N):
    n_queue.put(int(input()))

res_list = []
while n_queue.qsize() > 1:
    v1 = n_queue.get()
    v2 = n_queue.get()
    n_queue.put(v1+v2)
    res_list.append(v1+v2)

print(sum(res_list))

# heapq로 풀기 (240ms)
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

res_list = []
while len(heap) > 1:
    v1 = heapq.heappop(heap)
    v2 = heapq.heappop(heap)
    heapq.heappush(heap, v1+v2)
    res_list.append(v1+v2)

print(sum(res_list))
