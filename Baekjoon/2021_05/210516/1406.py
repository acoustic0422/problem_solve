"""
에디터
https://www.acmicpc.net/problem/1406
"""

import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node('?')
        self.tail = Node('?')
        self.head.next = self.tail
        self.tail.prev = self.head

    def init(self, word):
        curr = self.tail
        for c in word:
            node = Node(c)
            curr.prev.next = node
            node.prev = curr.prev
            node.next = curr
            curr.prev = node

    def typing(self, M):
        curr = self.tail
        for _ in range(M):
            cmd = sys.stdin.readline().strip()
            if cmd[0] == 'P':
                ch = cmd[2]
                node = Node(ch)
                curr.prev.next = node
                node.prev = curr.prev
                node.next = curr
                curr.prev = node

            elif cmd[0] == 'L':
                if curr.prev != self.head:
                    curr = curr.prev
            elif cmd[0] == 'D':
                if curr.next is not None:
                    curr = curr.next
            elif cmd[0] == 'B':
                if curr.prev != self.head:
                    prev = curr.prev.prev
                    prev.next = curr
                    curr.prev = prev

    def printWord(self):

        curr = self.head.next
        while curr != self.tail:
            if curr.next != self.tail:
                print(curr.data, end='')
            else:
                print(curr.data)
            curr = curr.next

word = sys.stdin.readline().strip()

ll = linkedList()
ll.init(word)

M = int(sys.stdin.readline())
ll.typing(M)
ll.printWord()
