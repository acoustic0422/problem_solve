"""
좌표 정렬하기2
https://www.acmicpc.net/problem/11651
"""

import sys

s = sys.stdin.readline()
N = int(s)

points = []
for _ in range(N):
    s = sys.stdin.readline()
    x,y = map(int, s.split())
    points.append((x,y))

points.sort(key=lambda a: (a[1],a[0]))

for x,y in points:
    print(x,y)
