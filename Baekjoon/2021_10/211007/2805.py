"""
나무 자르기
https://www.acmicpc.net/problem/2805
"""

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = 1000000000

maxheight = 0

while left <= right:
    mid = (left + right) // 2

    lumbers = sum( t - mid if t > mid else 0 for t in trees)

    if lumbers >= M:
        maxheight = mid
        left = mid + 1
    else:
        right = mid - 1

print(maxheight)