"""
https://leetcode.com/problems/network-delay-time/

k부터 출발해서 모든 노드가 신호를 받을 수 있는 시간을 리턴하라.
불가능할 경우 -1를 리턴한다.
입력값 (u, v, w)는 차례로 출발지, 도착지, 소요 시간으로 구성되며,
전체 노드 개수는 n이다.

times = [[2,1,1],[2,3,1],[4,5,1]]
N = 5
K = 2

times = [[1,2,1]]
n = 2
k = 2

times = [[3,1,5],[3,4,1],[3,2,2],[2,1,2],[4,5,1],[5,6,1],[6,7,1],[7,8,1]]
k = 3
n = 8

times = [[1,2,1],[2,1,3]]
n = 2
k = 2

다익스트라 알고리즘을 우선순위 큐를 사용해서 푼다. python에서는 heapq 라이브러리를 사용할 수 있다.
알고리즘 순서 : 
1) defaultdict로 구성한 노드 dict와 거리 dict를 준비한다.
2) 다음노드까지 걸린 시간과 해당 노드를 Q 리스트에서 우선순위 추출한다.
3) Q 리스트에서 꺼낸 노드가 이미 계산한 노드인지 확인한다.
4) 거리 리스트에 없다면 Q 리스트에 추가한다.
5) 1-4 반복
 
"""
# 아이디어01 : 모든 노드가 신호를 받는데 걸리는 시간을 계산한다.
# 아이디어02 : 시작 노드에서 모든 노드에 도달할 수 있는지 계산한다.
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list, n: int, k: int):
        node_list = defaultdict(list)
        for start_node, next_node, dist in times:
            node_list[start_node] += [(next_node, dist)]
        dist = defaultdict(int)
        Q = [(0, k)]  # (비용, 시작 노드)

        while Q:
            time, node = heapq.heappop(Q)
            # 우선순위 큐로 인해 항상 더 낮은 cost의 node 값이 기록되므로,
            # 탐색중인 node가 이미 dist에 있다는 것은 현재 cost가 더 크다는 것이다.
            if node not in dist:
                dist[node] = time
                for next_node, d in node_list[node]:
                    cost = time + d
                    heapq.heappush(Q, (cost, next_node))

        # n은 최종 노드가 아니다.
        # 따라서 k=2, n=2일 경우 k에서 n으로 가는 비용을 구하는 것이 아니라 2에서 시작해 전체 노드를 탐색하는 것을 뜻한다.
        # 전체 노드 수인 n과 비교함으로 전체 노드로 가는 비용을 구한 것인지 확인한다.
        if len(dist) == n:
            return max(dist.values())
        return -1
