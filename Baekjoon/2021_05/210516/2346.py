"""
풍선 터뜨리기
https://www.acmicpc.net/problem/2346
"""

class Node:
    def __init__(self,idx, data):
        self.idx = idx
        self.data = data
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n_node = 0

    def init(self, ballons):
        for idx, ballon in enumerate(ballons):
            node = Node(idx+1, ballon)
            if self.tail is None:
                self.head = node
                self.tail = node
                node.next = self.head
                node.prev = self.tail
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                node.next = self.head
                self.head.prev = node
            self.n_node += 1

    def play(self):
        result = []
        curr = self.head
        while self.n_node > 0:
            result.append(curr.idx)
            move = curr.data

            curr.prev.next = curr.next
            curr = curr.prev
            curr.next.prev = curr

            if move > 0:
                for _ in range(move):
                    curr = curr.next
            else:
                move = abs(move)
                for _ in range(move-1):
                    curr = curr.prev
            self.n_node -= 1
        return result



N = int(input())
ballons = list(map(int, input().split()))
ll = linkedList()
ll.init(ballons)
ans = ll.play()
print(*ans)
