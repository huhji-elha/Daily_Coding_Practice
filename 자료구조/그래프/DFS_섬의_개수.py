"""
https://leetcode.com/problems/number-of-islands/

1을 육지로, 0을 물로 가정한 2D 그리디 맵이 주어졌을 때, 섬의 개수를 계산하라.

> example01
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

> example02
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
# 아이디어 01 : 동,서,남,북으로 탐색한다.
# 아이디어 02 : 이미 탐색한 곳은 0으로 바꾼다.

# 첫번째 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        answer = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    answer += 1
                    self.dfs(i,j)
        return answer
    
    def dfs(self, i:int, j:int):
        if i<0 or j<0 or i>=len(self.grid) or j>=len(self.grid[0]) or self.grid[i][j] == "0":
            return
        self.grid[i][j] = "0"
        
        self.dfs(i, j+1) # 동
        self.dfs(i, j-1) # 서
        self.dfs(i+1, j) # 남
        self.dfs(i-1, j) # 북
        
# 두 번째 풀이: 함수를 좀 더 깔끔하게 바꾸기 (중첩 함수 이용)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i:int, j:int):
            if i<0 or j<0 or i>=len(grid) or \
            j>=len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
        
            dfs(i, j+1) # 동
            dfs(i, j-1) # 서
            dfs(i+1, j) # 남
            dfs(i-1, j) # 북
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    answer += 1
        return answer