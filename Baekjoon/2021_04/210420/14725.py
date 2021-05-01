"""
개미굴
https://www.acmicpc.net/problem/14725
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.depth = 0
        self.child = dict()

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, foods):
        curr = self.head

        depth = 0
        for f in foods[1:]:
            if f not in curr.child:
                curr.child[f] = Node(f)
                curr.child[f].depth = depth
            curr = curr.child[f]
            depth += 1

    def print_foods(self, cnode):
        curr = cnode

        if curr.key is not None:
            print('-'*2*curr.depth, end='')
            print(curr.key)

        food_list = sorted(curr.child.keys())
        for f in food_list:
            self.print_foods(curr.child[f])


import sys

s = sys.stdin.readline()
N = int(s)

trie = Trie()

for _ in range(N):
    s = sys.stdin.readline()
    line = list(s.strip().split())
    trie.insert(line)

trie.print_foods(trie.head)
