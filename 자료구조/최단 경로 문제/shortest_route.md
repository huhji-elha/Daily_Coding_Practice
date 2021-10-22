[🏠 main으로](../../README.md)

# 최단 경로 문제

```
💡 최단 경로 문제는 각 간선(Edge)의 가중치 합이 최소가 되는 두 정점(Node) 사이의 경로를 찾는 문제이다.
```

최단 경로는 지도 상의 한 지점에서 다른 지점으로 갈때 가장 빠른 길을 찾는 것과 유사한 문제이다.
내비게이션에서 목적지로 이동할 때 경로 탐색을 통해 나오는 최적 경로가 바로 최소 비용이 되는 최단 경로 문제이다.

정점(Vertex)은 교차로에 해당하고 간선(Edge)는 길에 해당한다.
가중치(weights)는 거리, 시간 등과 같은 이동 비용에 해당한다.

최단 경로 문제 중 가장 유명한 알고리즘은 다익스트라 알고리즘이다.


![](https://www.researchgate.net/profile/Atta-Ur-Rehman-6/publication/331484960/figure/fig1/AS:732550733512704@1551665113143/Illustration-of-Dijkstras-algorithm.ppm)
[__reference_link_](https://www.researchgate.net/publication/331484960_EMERGENCY_EVACUATION_GUIDANCE_SYSTEM_FOR_UNDERGROUND_MINERS)


---

## 다익스트라 알고리즘

다익스트라 알고리즘은 항상 노드 주변의 최단 경로만을 탐색하는 대표적인 Greedy 알고리즘이다.
단순하며 실행속도가 빠르다는 특징이 있다.
또한, 다익스트라 알고리즘은 노드 주변을 탐색할 때 BFS(너비 우선 탐색)을 이용한다.

다익스트라 알고리즘의 최초 구현에서는 시간 복잡도가 $O(V^2)$ 였으나,

현재는 BFS에서 가장 가까운 순서를 찾을 때 우선순위 큐를 적용하여 $O(V+E)logV)$ 로 줄었으며

모든 정점이 출발지에서 도달이 가능하다면 최종적으로 $O(E log V)$ 가 된다.