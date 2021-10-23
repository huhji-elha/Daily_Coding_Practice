"""
https://leetcode.com/problems/maximum-depth-of-binary-tree

주어진 이진 트리의 최대 깊이를 리턴.
TreeNode 구조를 사용할 것.

"""
# 아이디어 01: TreeNode 구조 이해하기.
# 아이디어 02: BSF로 구현하되, 양방향 추출이 빈번한 경우 데크 자료구조를 사용한다.
# (리스트보다 양방향 추출에서 실행속도가 빠름.)
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


"""
root = [3, 8, 20, None, None, 15, 7] 에 대하여
TreeNode는 다음과 같이 형성되어있다.

root = TreeNode(3)
a = TreeNode(8)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)

root.left = a
root.right = b
b.left = c
b.right = d

"""
