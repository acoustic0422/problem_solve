"""
행운의 바퀴
https://www.acmicpc.net/problem/2840
"""


class Node:
    def __init__(self,idx,ch):
        self.idx = idx
        self.data = ch
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n_node = 0

    def init(self, N):
        for idx in range(N):
            node = Node(idx, "?")
            if self.head is None:
                self.head = node
                self.tail = node
                node.prev = self.head
                node.next = self.tail
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                node.next = self.head
                self.head.prev = node


    def play(self, N, K):
        curr = self.head
        for _ in range(K):
            S, ch = input().strip().split()
            S = int(S)

            for _ in range(S):
                curr = curr.prev

            if curr.data == '?':
                curr.data = ch
            elif curr.data == ch:
                pass
            else:
                return '!'

        result = ""
        for _ in range(N):
            if curr.data != '?' and curr.data in result:
                return '!'
            else:
                result += curr.data
                curr = curr.next

        return result


N, K = map(int, input().split())
ll = linkedList()
ll.init(N)
print(ll.play(N,K))





