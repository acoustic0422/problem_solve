"""
스타트링크
https://www.acmicpc.net/problem/5014
"""

import sys
from collections import deque

s = sys.stdin.readline()
F,S,G,U,D = map(int, s.split())

if S < G and U == 0:
    print('use the stairs')
elif S > G and D == 0:
    print('use the stairs')
else:
    cnt = -1
    flag = 0

    q = deque()
    q.append(S)
    visited = set()
    visited.add(S)

    while q:
        cnt += 1
        l = len(q)
        for _ in range(l):
            curr = q.popleft()
            if curr == G:
                flag = 1
                break
            if curr+U <= F and curr + U not in visited:
                visited.add(curr+U)
                q.append(curr+U)
            if curr-D >= 1 and curr - D not in visited:
                visited.add(curr-D)
                q.append(curr-D)

        if flag == 1:
            break

    if flag == 1:
        print(cnt)
    else:
        print('use the stairs')