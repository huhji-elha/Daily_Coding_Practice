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
