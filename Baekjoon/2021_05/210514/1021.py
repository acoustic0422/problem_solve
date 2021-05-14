"""
회전하는 큐
https://www.acmicpc.net/problem/1021
링크드리스트 풀이
"""


class Node:
    def __init__(self):
        self.data = 0
        self.prev = None
        self.next = None


class linkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head.next
        self.count_node = 0

    def insert(self, data):
        newNode = Node()
        newNode.data = data
        if self.tail is None:
            self.head.next = newNode
            newNode.prev = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
        self.tail = newNode
        self.count_node += 1

    def popFront(self):
        if self.count_node > 0:
            delNode = self.head.next
            self.head.next = delNode.next
            if delNode.next is not None:
                delNode.next.prev = self.head
            delNode.next = None
            self.count_node -= 1

    def frontToBack(self):
        if self.count_node > 0:
            tNode = self.head.next
            self.head.next = tNode.next
            tNode.next = None
            tNode.prev = self.tail
            self.tail.next = tNode
            self.tail = tNode

    def backToFront(self):
        if self.count_node > 0:
            tNode = self.tail
            self.tail = tNode.prev
            tNode.prev = self.head
            tNode.next = self.head.next
            self.head.next.prev = tNode
            self.head.next = tNode


N,M = map(int, input().split())
targets = list(map(int, input().split()))

ll = linkedList()
for i in range(1, N+1):
    ll.insert(i)

cnt = 0
for t in targets:
    if t == ll.head.next.data:
        ll.popFront()
    else:
        dist = 0
        curr = ll.head.next
        while curr.data != t:
            curr = curr.next
            dist += 1
        if dist <= ll.count_node//2:
            while dist:
                dist -= 1
                ll.frontToBack()
                cnt += 1
        else:
            dist = ll.count_node - dist
            while dist:
                dist -= 1
                ll.backToFront()
                cnt += 1
        ll.popFront()

print(cnt)