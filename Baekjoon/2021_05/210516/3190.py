"""
뱀
https://www.acmicpc.net/problem/3190
"""

import sys

delta = [(1,0), (0,1), (-1,0), (0,-1)]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

class Snake:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        init = Node(1,1)
        self.head.next = init
        init.prev = self.head
        init.next = self.tail
        self.tail.prev = init

        self.dir = 0
        self.body = set()
        self.body.add((1,1))

        self.apple = set()

    def addApple(self, x, y):
        self.apple.add((x,y))

    def turn(self, cmd):
        if cmd == 'D':
            self.dir = (self.dir + 1) % 4
        elif cmd == 'L':
            self.dir = (self.dir + 4 - 1) % 4

    def move(self, N):
        x = self.head.next.x
        y = self.head.next.y
        nx, ny = x + delta[self.dir][0], y + delta[self.dir][1]

        if nx < 1 or nx > N or ny < 1 or ny > N:
            return -1

        if (nx,ny) in self.body:
            return -1

        newHead = Node(nx, ny)
        self.head.next.prev = newHead
        newHead.next = self.head.next
        self.head.next = newHead
        newHead.prev = self.head
        self.body.add((nx, ny))
        if (nx,ny) in self.apple:
            self.apple.remove((nx,ny))
        else:
            dx = self.tail.prev.x
            dy = self.tail.prev.y
            self.body.remove((dx,dy))

            prev = self.tail.prev.prev
            prev.next = self.tail
            self.tail.prev = prev

        return 1


N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

snake = Snake()

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    snake.addApple(x,y)

L = int(sys.stdin.readline())

turnCmds = []
for _ in range(L):
    X, C = sys.stdin.readline().strip().split()
    X = int(X)
    turnCmds.append((X,C))

turnCmds = turnCmds[::-1]

time = 0
while True:
    time += 1
    if snake.move(N) == -1:
        break

    if turnCmds and turnCmds[-1][0] == time:
        snake.turn(turnCmds[-1][1])
        turnCmds.pop()

print(time)