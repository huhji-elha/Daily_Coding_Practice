"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능 구현.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
"""

# 아이디어 01 : serialize에서는 각 계층의 노드들을 차례로 탐색해야하기 때문에 BFS를 사용한다.
# 아이디어 02 : deserialize에서는 BFS를 사용하되, 입력받은 data의 index값을 사용한다.
# Runtime : 269 ms
# Memory : 18.7 MB
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str():
        queue = collections.deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        return ' '.join(result)

    def deserialize(self, data) -> TreeNode():
        nodes = data.split()  # str로 입력되었으므로 리스트로 바꿔준다.
        root = TreeNode(nodes[0])
        queue = collections.deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if nodes[idx] is not "#":  # 다음 노드가 있는지 미리 탐색한다.
                node.left = TreeNode(nodes[idx])
                queue.append(node.left)
            idx += 1
            if nodes[idx] is not "#":
                node.right = TreeNode(nodes[idx])
                queue.append(node.right)
            idx += 1
        return root
