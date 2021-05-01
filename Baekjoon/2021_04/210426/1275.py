"""
커피숍2
https://www.acmicpc.net/problem/1275
** 정답 찾아봄
https://hooongs.tistory.com/119
** Segment Tree
https://www.acmicpc.net/blog/view/9
"""


class SegTree:
    def __init__(self, N, A):
        self.A = A
        self.tree = [0 for _ in range(4 * N)]
        self.init(1, 0, N - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.A[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.init(node * 2, start, mid) + self.init(node * 2 + 1, mid + 1, end)
        return self.tree[node]

    def update(self, node, start, end, idx, diff):
        if idx < start or end < idx:
            return

        self.tree[node] += diff

        if not start == end:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, idx, diff)
            self.update(node * 2 + 1, mid + 1, end, idx, diff)

    def sum(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.sum(node * 2, start, mid, left, right) + self.sum(node * 2 + 1, mid + 1, end, left, right)


import sys

s = sys.stdin.readline()
N, Q = map(int, s.split())

s = sys.stdin.readline()
A = list(map(int, s.split()))

st = SegTree(N, A)

for _ in range(Q):
    s = sys.stdin.readline()
    x, y, a, b = map(int, s.split())
    if x > y:
        x, y = y, x
    print(st.sum(1, 0, N - 1, x - 1, y - 1))
    st.update(1, 0, N - 1, a - 1, b - A[a - 1])
    A[a - 1] = b
