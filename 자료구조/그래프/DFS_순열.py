"""
https://leetcode.com/problems/permutations/

서로 다른 정수를 입력받아 가능한 모든 순열 리턴

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
"""

# 아이디어01 : dfs 재귀함수로 순열 풀기
# 한 번 사용한 숫자는 리스트에서 제거 --> 다음 재귀 함수로 넘긴다(next) --> 제거한 숫자는 순열에 추가한다.
# Runtime : 52 ms
# Memory : 14.5 MB
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        next_nums = []
        permute_list = []
        answer = []

        def dfs(nums):
            if len(nums) == 0:
                answer.append(permute_list[:]) # 반드시 리스트 전체 복사를 해서 append 해야한다.
                # answer.append(permute_list)로 하면 answer의 모든 permute_list가 하나의 permute_list를 참조하므로
                # permute_list의 마지막 상태인 빈 리스트만 담기게 된다.

            for n in nums:
                next_nums = nums[:] # 이것 역시 다음 재귀 함수로 넘기는 next_nums를 전체 복사 해야한다.
                                    # 파이썬은 문자열이 불변 객체이며 참조를 하는 형태이기 때문이다.
                next_nums.remove(n)
                permute_list.append(n)
                dfs(next_nums)
                permute_list.pop()
        dfs(nums)
        return answer
    
# 아이디어02 : python의 itertools.permutation으로 풀이하기
# Runtime : 58 ms
# Memory : 14.5 MB
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda x:list(x), permutations(nums)))
