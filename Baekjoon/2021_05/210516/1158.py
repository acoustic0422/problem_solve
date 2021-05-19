"""
요세푸스 문제
https://www.acmicpc.net/problem/1158
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n_node = 0

    def init(self, N):
        for i in range(1, N + 1):
            node = Node(i)
            if self.tail is None:
                self.tail = node
                self.head = node
                node.next = self.head
            else:
                self.tail.next = node
                self.tail = node
                self.tail.next = self.head
                node.next = self.head
            self.n_node += 1

    def yosephus(self, K):
        curr = self.tail
        prev = curr
        print("<", end='')
        while self.n_node > 0:
            for _ in range(K):
                prev = curr
                curr = curr.next
            if self.n_node != 1:
                print(curr.data, end=', ')
            else:
                print(curr.data, end='')
            prev.next = curr.next
            curr.next = None
            curr = prev
            self.n_node -= 1

        print(">")


N, K = map(int, input().split())
ll = linkedList()
ll.init(N)
ll.yosephus(K)
