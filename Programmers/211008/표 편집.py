"""
표 편집
https://programmers.co.kr/learn/courses/30/lessons/81303
"""

import heapq

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    upHeap = []
    downHeap = []
    trashcan = []

    for i in range(n):
        heapq.heappush(downHeap, i)

    for _ in range(k):
        num = heapq.heappop(downHeap)
        heapq.heappush(upHeap, -num)

    for c in cmd:
        if c[0] == 'U':
            _, iter = c.split()
            iter = int(iter)
            while upHeap and iter > 0:
                num = -heapq.heappop(upHeap)
                heapq.heappush(downHeap, num)
                iter -= 1

        elif c[0] == 'D':
            _, iter = c.split()
            iter = int(iter)
            while len(downHeap) > 1 and iter> 0:
                num = heapq.heappop(downHeap)
                heapq.heappush(upHeap, -num)
                iter -= 1
        elif c[0] == 'C':
            num = heapq.heappop(downHeap)
            trashcan.append(num)
            if not downHeap and upHeap:
                num = heapq.heappop(upHeap)
                heapq.heappush(downHeap, -num)
        elif c[0] == 'Z':
            num = trashcan.pop()
            if downHeap[0] > num:
                heapq.heappush(upHeap, -num)
            else:
                heapq.heappush(downHeap, num)

    for t in trashcan:
        answer[t] = 'X'

    return "".join(answer)


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))
