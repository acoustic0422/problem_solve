"""
가운데를 말해요
https://www.acmicpc.net/problem/1655
"""

import sys
import heapq

s = sys.stdin.readline()
N = int(s)

max_heap = []
min_heap = []

for _ in range(N):
    s = sys.stdin.readline()
    num = int(s)
    heapq.heappush(max_heap,(-num,num))

    if len(min_heap) < len(max_heap):
        _, temp = heapq.heappop(max_heap)
        heapq.heappush(min_heap,(temp, temp))
        print(min_heap[0][1])
    elif len(min_heap) == len(max_heap):
        _, temp = heapq.heappop(max_heap)
        heapq.heappush(min_heap, (temp,temp))
        _, temp = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-temp, temp))
        print(min(min_heap[0][1], max_heap[0][1]))

