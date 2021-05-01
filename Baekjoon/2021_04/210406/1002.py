"""
터렛
https://www.acmicpc.net/problem/1002
"""
import math

N = int(input())

for _ in range(N):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if r1 > r2:
        r2, r1 = r1, r2

    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist == r1 + r2:
        print(1)
    elif dist > r1+r2:
        print(0)
    elif dist < r1+r2:
        if dist > r2 - r1:
            print(2)
        elif dist == r2 - r1:
            print(1)
        elif dist < r2 - r1:
            print(0)


