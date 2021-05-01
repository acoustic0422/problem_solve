"""
좌표 정렬하기
https://www.acmicpc.net/problem/11650
"""

import sys

s = sys.stdin.readline()
N = int(s)

points = []
for _ in range(N):
    s = sys.stdin.readline()
    x,y = map(int, s.split())
    points.append((x,y))

points.sort(key=lambda a: (a[0],a[1]))

for x,y in points:
    print(x,y)
