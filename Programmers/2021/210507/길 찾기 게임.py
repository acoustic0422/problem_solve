"""
길 찾기 게임
https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3
"""

import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None
        self.t_result = []

    def Insert(self, x, y, idx):
        node = Node(x, y, idx)

        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while True:
                if curr.x > node.x:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                elif curr.x < node.x:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    def pre_traverse(self, curr):
        self.t_result.append(curr.idx)
        if curr.left is not None:
            self.pre_traverse(curr.left)
        if curr.right is not None:
            self.pre_traverse(curr.right)

    def post_traverse(self, curr):
        if curr.left is not None:
            self.post_traverse(curr.left)
        if curr.right is not None:
            self.post_traverse(curr.right)
        self.t_result.append(curr.idx)


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    nodeinfo.sort(key=lambda a: a[1], reverse=True)

    tree = Tree()
    for info in nodeinfo:
        x, y, idx = info
        tree.Insert(x, y, idx)

    tree.t_result = []
    tree.pre_traverse(tree.root)

    answer = [tree.t_result]

    tree.t_result = []
    tree.post_traverse(tree.root)
    answer.append(tree.t_result)

    return answer


# nodeinfo = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]
nodeinfo = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
# nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
# nodeinfo = [[5, 3]]
print(solution(nodeinfo))
