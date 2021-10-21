"""
https://leetcode.com/problems/subsets/

모든 부분 집합 나열하기

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

"""

# 첫번째 풀이
# 아이디어 : 조합을 만들면서 생성되는 모든 리스트를 저장하기 / idx를 사용해서 중복 없는 조합 만들기
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num_sets = []
        def subset(idx, next_set):
            num_sets.append(next_set[:])
            for i in range(idx, len(nums)):
                next_set.append(nums[i])
                subset(i+1, next_set)
                next_set.pop()
        subset(0,[])
        return num_sets

# 두 번째 풀이
# 재귀 함수의 특성을 사용하여 코드 정리하기 --> next_set을 재귀 함수 input에서 처리하기
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num_sets = []
        def subset(idx, path):
            num_sets.append(path)
            for i in range(idx, len(nums)):
                subset(i+1, path+[nums[i]])
        subset(0,[])
        return num_sets