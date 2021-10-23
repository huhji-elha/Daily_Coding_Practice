"""
https://leetcode.com/problems/diameter-of-binary-tree

이진 트리에서 두 노드 간 가장 긴 경로 찾기

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

"""
# 아이디어 01: root 노드에서 tree의 끝까지 가는 dfs 재귀함수를 구현한다.
# 아이디어 02: tree의 깊이와 경로 길이를 각각 따로 구해야한다.
# 경로 = left의 깊이 + right의 깊이
# 깊이 = max(left의 깊이, right의 깊이) + 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode):
        self.distance = 0
        # dfs 함수에서 distance 변수에 재할당을 해주므로 로컬 변수가 아니라 클래스 변수로 선언해야한다.

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.distance = max(self.distance, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.distance
