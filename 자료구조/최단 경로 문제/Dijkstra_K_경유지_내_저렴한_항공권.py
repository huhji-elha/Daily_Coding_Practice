"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/

시작 노드에서 도착 노드까지의 가장 저렴한 가격을 계산하되, 
K 경유지 이내에 도착하는 가격을 리턴.
존재하지 않을 경우 -1을 리턴.

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

n = 5
flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
src = 0
dst = 4
k = 1

"""

# 아이디어01 : 네트워크 딜레이 타임에서 사용한 다익스트라 알고리즘을 변형해서 사용한다.
# k 이내에 도착하는 가장 작은 cost를 구하는 것이므로 우선순위 큐에 K 값도 반영한다.
# 도착 노드에 도착한 즉시 cost를 반환하면 되므로 모든 경로를 기록하는 dist dict는 사용하지 않아도 된다.
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int):
        edges = defaultdict(list)
        dst_list = []
        for u, v, w in flights:
            if v == dst:
                dst_list.append(v)
            edges[u].append((v, w))

        if not dst_list:  # dst로 가는 경로가 존재하지 않는 경우 -1을 반환한다.
            return -1
        Q = [(0, src, k)]  # cost, start_node, k

        while Q:
            price, node, K = heapq.heappop(Q)
            if node == dst:  # 우선순위 큐의 특징을 사용하기 때문에 이때의 price와 K가 가장 작다.
                return price
            if K >= 0:
                for v, w in edges[node]:
                    flight_cost = price + w
                    heapq.heappush(Q, (flight_cost, v, K - 1))
        return -1
