[🏠 main으로](../../README.md)

# 그래프 자료구조

```
💡 그래프란 Vertex(정점)와 Edge(간선)이 서로 연결되어 있는 집합 구조를 말한다
```

- [그래프 자료구조](#그래프-자료구조)
  - [오일러 경로](#오일러-경로)
  - [해밀턴 경로](#해밀턴-경로)
  - [그래프 순회](#그래프-순회)
    - [DFS (깊이 우선 탐색)](#dfs-깊이-우선-탐색)
    - [BFS (너비 우선 탐색)](#bfs-너비-우선-탐색)
    - [백트래킹](#백트래킹)
    - [DFS 기본 알고리즘 풀이](#dfs-기본-알고리즘-풀이)

---
## 오일러 경로
모든 간선을 한 번씩 방문하는 유한 그래프(Finite Graph)를 오일러 경로라 한다.

'한붓 그리기'라고도 한다.


## 해밀턴 경로

해밀턴 경로는 각 정점을 한 번씩 방문하는 그래프 경로를 말한다.
해밀턴 경로를 찾는 문제는 최적 알고리즘이 없는 대표적인 난해 문제이다.

외판원 문제(TSP)라고도 불린다.


## 그래프 순회
### DFS (깊이 우선 탐색)

일반적으로 DFS는 스택으로 구현하며, 재귀를 사용하면 더 간단하게 구현할 수 있다.

```python
graph = { 1: [2, 3, 4],
          2: [5],
          3: [5],
          4: [],
          5: [6,7],
          6: [],
          7: [3]}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```

### BFS (너비 우선 탐색)

BFS는 큐로 구현한다. 모든 인접 간선을 추출하고 도착점인 정점을 큐에 삽입하는 방식이다.

👉 BFS는 재귀로 동작하지 않는다.

```python
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```
### 백트래킹

백트래킹은 DFS와 같은 방식으로 탐색하다 더 갈 수 없으면 왔던 길을 되돌아가는 방식의 알고리즘이다.
백트래킹은 주로 재귀로 구현한다.

---

### DFS 기본 알고리즘 풀이
* [DFS로 이중 배열 탐색하기](./DFS_섬의_개수.py)
* [DFS로 조합 구현하기](./DFS_조합.py)
* [DFS로 순열 구현하기](./DFS_순열.py)
* [DFS 조합 응용 - 중복 조합 그래프 탐색](./DFS_조합의_합.py)
* [DFS 조합 응용 - 트리 탐색](./DFS_부분집합.py)
* [DFS 조합 응용 - 백트래킹](./DFS_전화번호_문자_조합.py)
* [DFS 조합 응용 - 순서가 있는 조합](./DFS_일정_재구성.py)
* [DFS 응용 - 순환 그래프 구현](./DFS_코스_스케줄.py)