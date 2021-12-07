"""
https://leetcode.com/problems/combinations/

전체 수 n을 입력받아 k개의 조합 리턴

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

# 아이디어01 : 재귀 함수로 DFS 구현하기
# Runtime : 581 ms
# Memory : 15.8 MB


class Solution:
    def combine(self, n: int, k: int):
        answer = []
        next_comb = []
        nums = list(range(1, n+1))

        def comb(nums, next_comb):
            if len(next_comb) == k:
                # 객체 복사해서 넣어주기 / 복사하지 않으면 최종 next_comb 형태인 빈 리스트만 추가된다.
                answer.append(next_comb[:])
                return
            for i, n in enumerate(nums):
                next_comb.append(n)
                # 중복을 허용하지 않으므로 추가한 값을 제외한 다음 리스트를 넘긴다.
                comb(nums[i+1:], next_comb)
                next_comb.pop()
        comb(nums, [])
        return answer

# 아이디어02 : python의 itertools.combinations로 풀기
# Runtime : 68 ms
# Memory : 	15.6 MB


class Solution:
    def combine(self, n: int, k: int):
        return list(map(list, combinations(range(1, n+1), k)))
