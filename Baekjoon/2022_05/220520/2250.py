import sys

input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self,num):
        self.num = num
        self.col = -1
        self.left = None
        self.right = None
        self.parent = None

nodelist = [None for _ in range(N+1)]

for _ in range(N):
    p, l, r = map(int, input().split())
    if nodelist[p] is None:
        nodelist[p] = Node(p)
    if nodelist[l] is None and l != -1:
        nodelist[l] = Node(l)
    if nodelist[r] is None and r != -1:
        nodelist[r] = Node(r)

    if l != -1:
        nodelist[p].left = nodelist[l]
        nodelist[l].parent = nodelist[p]
    if r != -1:
        nodelist[p].right = nodelist[r]
        nodelist[r].parent = nodelist[p]


root = 1
while nodelist[root].parent is not None:
    root = nodelist[root].parent.num

cnt = 1


def inorder(curr):
    if nodelist[curr].left is not None:
        inorder(nodelist[curr].left.num)
    global cnt
    nodelist[curr].col = cnt
    cnt += 1
    if nodelist[curr].right is not None:
        inorder(nodelist[curr].right.num)


inorder(root)

levelwidth = dict()

def widthcheck(curr, lvl):
    global levelwidth
    if lvl not in levelwidth:
        levelwidth[lvl] = [N+1, -1]
    levelwidth[lvl][0] = min(levelwidth[lvl][0], nodelist[curr].col)
    levelwidth[lvl][1] = max(levelwidth[lvl][1], nodelist[curr].col)
    if nodelist[curr].left is not None:
        widthcheck(nodelist[curr].left.num, lvl+1)
    if nodelist[curr].right is not None:
        widthcheck(nodelist[curr].right.num, lvl+1)


widthcheck(root, 1)

result = [-1, -1]
maxwidth = -1

for lv in levelwidth:
    if levelwidth[lv][1] - levelwidth[lv][0] + 1 > maxwidth:
        maxwidth = levelwidth[lv][1] - levelwidth[lv][0] + 1
        result[0] = lv
        result[1] = maxwidth

print(*result)