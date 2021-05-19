"""
키로거
https://www.acmicpc.net/problem/5397
"""

import sys

class Node:
    def __init__(self, ch):
        self.data = ch
        self.prev = None
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node('?')
        self.tail = Node('?')
        self.head.next = self.tail
        self.tail.prev = self.head

    def typing(self, cmd):
        curr = self.tail

        for c in cmd:
            if c == '<':
                if curr.prev != self.head:
                    curr = curr.prev
            elif c == '>':
                if curr.next is not None:
                    curr = curr.next
            elif c == '-':
                if curr.prev != self.head:
                    prev = curr.prev.prev
                    prev.next = curr
                    curr.prev = prev
            else:
                node = Node(c)
                curr.prev.next = node
                node.prev = curr.prev
                curr.prev = node
                node.next = curr

        curr = self.head.next
        while curr != self.tail:
            print(curr.data, end='')
            curr = curr.next
        print()


T = int(sys.stdin.readline())

for tc in range(T):
    ll = linkedList()
    cmd = sys.stdin.readline().strip()
    ll.typing(cmd)