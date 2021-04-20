"""
전화번호 목록
https://www.acmicpc.net/problem/5052
"""

class node(object):
    def __init__(self, key, isEnd):
        self.key = key
        self.isEnd = isEnd
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.head = node(None, False)

    def insert(self, string):
        curr = self.head

        for ch in string:
            if ch not in curr.children:
                curr.children[ch] = node(ch, False)
            curr = curr.children[ch]

        curr.isEnd = True

    def checkDuplicate(self, string):
        curr = self.head
        for ch in string:
            if ch in curr.children:
                curr = curr.children[ch]

        if curr.isEnd and curr.children:
            return False
        else:
            return True

import sys

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    N = int(s)
    trie = Trie()

    numbers = []
    for _ in range(N):
        s = sys.stdin.readline()
        trie.insert(s.strip())
        numbers.append(s.strip())

    flag = 0
    for num in numbers:
        if trie.checkDuplicate(num) == False:
            flag = 1
            break

    if flag == 1:
        print('NO')
    else:
        print('YES')