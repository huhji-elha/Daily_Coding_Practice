"""
https://leetcode.com/problems/course-schedule/

0을 완료하기 위해 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력을 받았을 때 모든 코스가 완료 가능한지 판별하라.
"""
# 아이디어01 : 순환 그래프인지 판별하기
# 재귀 함수와 DFS로 순환 그래프 판별 알고리즘 구현.
# 재귀 함수에서 False를 리턴하기 위해서는 상위 함수로 False를 전달해주어야한다.
# [[0, 1], [0, 2], [1, 2]]은 순환구조가 아니라는 것을 주의하자.

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list):
        finished = set()
        pred = defaultdict(list)
        for p in prerequisites:
            pred[p[0]] += [p[1]]

        def dfs(s):
            if s in finished:
                return False
            finished.add(s)
            # pred를 defaultdict로 생성했기 때문에 딕셔너리의 빈 값 조회시 NULL 오류가 발생하지 않는다.
            for i in pred[s]:
                if not dfs(i):
                    return False
            finished.remove(s)
            return True

        for p in prerequisites:
            if not dfs(p[0]):
                return False

        return True

# 아이디어02 : 위의 방법대로 하면 이미 탐색한 노드를 여러번 반복해서 탐색하게된다.
# 가령, [[0,2],[1,2],[2,3],[3,4]] 의 트리를 탐색한다고 했을때 0에서 시작하는 루트와 1에서 시작하는 루트가 같음에도 두 번 탐색하게 되는 것.
# 따라서 이미 탐색을 마친 노드라는 것을 중간에 알면 탐색을 중단하고 True를 반환해야한다.


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: list):
        pre_dict = defaultdict(list)
        for p in prerequisites:
            pre_dict[p[0]] += [p[1]]

        searched = set()  # 한번 방문한 노드 : 순환 구조 판별용
        visited = set()  # 판별이 끝난 노드 : 재탐색 방지용

        def dfs(node):
            if node in searched:
                return False
            if node in visited:
                return True
            searched.add(node)
            for i in pre_dict[node]:
                if not dfs(i):
                    return False
            # 새로 탐색하는 노드가 순환 구조가 아닐 때 여기로 넘어온다.
            searched.remove(node)  # 한번 방문한 노드는 삭제한다.
            visited.add(node)  # 순환 구조가 아닌 노드는 저장한다.
            return True

        for i in list(pre_dict):  # 트리의 시작점이 여러 곳일 수 있으므로 for문으로 전체 탐색한다.
            if not dfs(i):
                return False
        return True
