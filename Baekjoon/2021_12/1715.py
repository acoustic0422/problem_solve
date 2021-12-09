"""
1715
https://www.acmicpc.net/problem/1715
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())

ncards = []
for _ in range(N):
    ncards.append(int(input()))

heapq.heapify(ncards)

num_compare = 0

while len(ncards) > 1:
    first = heapq.heappop(ncards)
    second = heapq.heappop(ncards)
    next = first + second
    num_compare += next
    heapq.heappush(ncards, next)

print(num_compare)

