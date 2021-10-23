"""
https://leetcode.com/problems/invert-binary-tree/

주어진 이진트리를 반전해서 리턴

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
# 아이디어 01 : bfs를 데크로 구현한 알고리즘 응용하기
# 주의사항 : 노드 값을 뒤집는 것이 아니라 트리 구조 자체를 뒤집는 것이다. -> root를 리턴해야한다.
import collections


class Solution:
    def invertTree(self, root: TreeNode):
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                # 왼쪽 노드와 오른쪽 노드 값을 바꿔준다.
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

