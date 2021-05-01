"""
보석 도둑
https://www.acmicpc.net/problem/1202
"""

import sys
import heapq

s = sys.stdin.readline()
N,K = map(int, s.split())

jems = []
jems_v = []
bags = []

for _ in range(N):
    s = sys.stdin.readline()
    M, V = map(int, s.split())
    heapq.heappush(jems, (M,V))

for _ in range(K):
    s = sys.stdin.readline()
    bags.append(int(s))

bags.sort()

total_value = 0
for n in bags:
    while jems and n >= jems[0][0]:
        M,V = heapq.heappop(jems)
        heapq.heappush(jems_v, (-V, M))

    if jems_v:
        V, M = heapq.heappop(jems_v)
        total_value -= V

print(total_value)


