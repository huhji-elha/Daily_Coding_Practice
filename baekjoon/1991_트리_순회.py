import sys
input = sys.stdin.readline
N = int(input())
tree = []


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):  # 전위순회 - 해당 노드 먼저 출력, 그 후 좌-우 재귀
    print(node.data, end='')
    if node.left != '':
        pre_order(node.left)
    if node.right != '':
        pre_order(node.right)


def in_order(node):  # 중위 순회 - 왼쪽 재귀 후 노드 출력, 마지막으로 오른쪽 노드 재귀
    if node.left != '':
        in_order(node.left)
    print(node.data, end='')
    if node.right != '':
        in_order(node.right)


def post_order(node):  # 후위 순회 - 좌-우 재귀 후 마지막으로 노드 출력
    if node.left != '':
        post_order(node.left)
    if node.right != '':
        post_order(node.right)
    print(node.data, end='')


for i in range(N):
    data = input().split()
    node = Node(data[0])
    if data[1] == ".":
        data[1] = ""
    if data[2] == ".":
        data[2] = ""

    node.left = data[1]
    node.right = data[2]

    tree.append(node)

for i in range(N):
    for j in range(N):
        if tree[i].data == tree[j].left:
            tree[j].left = tree[i]
        elif tree[i].data == tree[j].right:
            tree[j].right = tree[i]

pre_order(tree[0])
print()
in_order(tree[0])
print()
post_order(tree[0])
