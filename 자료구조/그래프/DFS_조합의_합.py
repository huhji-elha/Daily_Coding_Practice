"""
https://leetcode.com/problems/combination-sum/

숫자 집합 condidates를 조합해 합이 target이 되는 원소 나열.
각 원소는 중복으로 나열 가능하다.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""

# 아이디어01 : 재귀 DFS로 조합 풀기 / 단, idx를 사용해서 중복이 안되게 하기.
# Runtime : 137 ms
# memory : 14.5 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def comb_sum(idx, next_comb):
            if sum(next_comb) == target:
                answer.append(next_comb[:])
                return
            if sum(next_comb) > target:
                return
            for i in range(idx, len(candidates)):
                next_comb.append(candidates[i]) 
                comb_sum(i, next_comb)
                next_comb.pop()
        comb_sum(0, [])
        return answer

# 재귀함수의 특징을 더 살려서 코드 정리하기 + sum은 O(N)을 가지므로 더 효율적인 방법 찾아보기
# Runtime : 73 ms
# Memory : 	14.4 MB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def comb_sum(csum, idx, path):
            if csum < 0:
                return
            if csum == 0:
                answer.append(path)
                return
            for i in range(idx, len(candidates)):
                comb_sum(csum - candidates[i], i, path + [candidates[i]])
        comb_sum(target, 0, [])
        return answer