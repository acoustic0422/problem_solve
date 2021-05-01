"""
DSLR
https://www.acmicpc.net/problem/9019
"""

import sys
from collections import deque


def calc(num, op):
    if op == 'L':
        temp = num % 1000
        temp2 = num // 1000
        num = temp*10 + temp2
    elif op == 'R':
        temp = num // 10
        temp2 = num % 10
        num = temp2 * 1000 + temp
    elif op == 'D':
        num *= 2
        if num > 9999:
            num = num % 10000
    elif op == 'S':
        if num == 0:
            num = 9999
        else:
            num -= 1

    return num


s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    start, goal = map(int, s.split())
    q = deque()
    q.append((start, ''))
    visited = [0 for _ in range(10000)]
    visited[start] = 1
    while q:
        now, his = q.popleft()
        if now == goal:
            print(his)
            break
        for ch in 'DSLR':
            cand = calc(now, ch)
            if visited[cand] == 0:
                visited[cand] = 1
                q.append((cand, his+ch))
