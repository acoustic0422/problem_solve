"""
열쇠
https://www.acmicpc.net/problem/9328
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]
alpha = 'abcdefghijklmnopqrstuvwxyz'


def search_doc(q, floor, keys):
    steal_docs = 0
    visited = set()

    while q:
        flag = 0
        y,x = q.popleft()
        for dy, dx in delta:
            if 0 <= x+dx < w+2 and 0<= y+dy < h+2 and (y+dy, x+dx) not in visited:
                if floor[y+dy][x+dx] == '.' or floor[y+dy][x+dx] in keys:
                    visited.add((y+dy, x+dx))
                    q.append((y+dy, x+dx))
                elif floor[y+dy][x+dx] in alpha:
                    keys.add(floor[y+dy][x+dx].upper())
                    floor[y+dy][x+dx] = '.'
                    sy, sx = y+dy, x+dx
                    flag = 1
                    break
                elif floor[y+dy][x+dx] == '$':
                    visited.add((y+dy, x+dx))
                    floor[y+dy][x+dx] = '.'
                    steal_docs += 1
                    q.append((y+dy, x+dx))
        if flag == 1:
            visited.clear()
            visited.add((sy,sx))
            q.clear()
            q.append((sy,sx))

    return steal_docs


s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    h,w = map(int, s.split())
    floor = []
    floor.append(list('.'*(w+2)))
    for _ in range(h):
        s = sys.stdin.readline()
        line = list('.' + s.strip() + '.')
        floor.append(line)
    floor.append(list('.'*(w+2)))

    s = sys.stdin.readline()
    k = s.strip()
    keys = set()
    if k != '0':
        for ch in k:
            keys.add(ch.upper())

    q = deque()
    q.append((0,0))

    num_docs = 0
    num_docs += search_doc(q,floor,keys)

    print(num_docs)




