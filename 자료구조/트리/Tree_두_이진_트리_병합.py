"""
https://leetcode.com/problems/merge-two-binary-trees/

주어진 이진트리를 병합하되, 같은 위치에 있는 노드는 값을 합한다.

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

"""

# 아이디어 01 : 재귀함수와 TreeNode 클래스를 사용해서 새로운 트리를 구성한다.
# 아이디어 02 : root1와 root2가 같은 위치에 노드가 있으면 합치고, 하나라도 없으면 있는 것을 반환한다.
# Runtime : 121 ms
# Memory : 15.3 MB
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTree(self, root1: TreeNode, root2: TreeNode):
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)  # TreeNode를 사용해서 새롭게 노드를 정의한다.
            node.left = self.mergeTree(root1.left, root2.left)
            node.right = self.mergeTree(root1.right, root2.right)
            return node
        else:
            return root1 or root2  # 둘 중 None 값이 아닌 node가 리턴된다.

