"""
길 찾기 게임
https://programmers.co.kr/learn/courses/30/lessons/42892
"""
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, point):
        self.left = None
        self.right = None
        self.point = point

class Tree:
    def __init__(self):
        self.Root = None
        self.Pre = []
        self.Post = []

    def insert(self, point):
        node = Node(point)
        if self.Root is None:
            self.Root = node
        else:
            pos = self.Root
            while True:
                if pos.point[0] > node.point[0]:
                    if pos.left is None:
                        pos.left = node
                        break
                    else:
                        pos = pos.left
                else:
                    if pos.right is None:
                        pos.right = node
                        break
                    else:
                        pos = pos.right

    def preorder(self, root):
        self.Pre.append(root.point[2])
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)

    def postorder(self, root):
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        self.Post.append(root.point[2])



def solution(nodeinfo):
    answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    tree = Tree()
    for n in nodeinfo:
        tree.insert(n)

    tree.preorder(tree.Root)
    tree.postorder(tree.Root)
    answer.append(tree.Pre)
    answer.append(tree.Post)

    return answer


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))