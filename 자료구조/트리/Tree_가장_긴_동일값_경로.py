"""
https://leetcode.com/problems/longest-univalue-path/

동일한 값을 가진 가장 긴 경로 찾기

Input: root = [5,4,5,1,1,5]
Output: 2

"""
# 아이디어 01 : 앞서 풀었던 이진 트리의 직경 알고리즘을 응용한다.
# 아이디어 02 : 현재 노드와 자식 노드의 값을 비교해서 거리 값을 업데이트하거나 초기화한다.
# Runtime : 388 ms
# Memory : 18.1 MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드와 자식 노드의 값을 비교해서 left, right 업데이트
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result
