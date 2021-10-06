"""
이중우선순위큐
https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
"""

import heapq
from collections import defaultdict

def solution(operations):
    answer = [0,0]
    maxhq = []
    minhq = []

    numberdict = defaultdict(int)

    for op in operations:
        d, n = op.split()
        if d == 'I':
            heapq.heappush(maxhq, -int(n))
            heapq.heappush(minhq, int(n))
            numberdict[int(n)] += 1
        elif d == 'D':
            if n == '1':
                while maxhq and numberdict[-maxhq[0]] <= 0:
                    heapq.heappop(maxhq)
                if maxhq:
                    num = -heapq.heappop(maxhq)
                    numberdict[num] -= 1

            elif n == '-1':
                while minhq and numberdict[minhq[0]] <= 0:
                    heapq.heappop(minhq)
                if minhq:
                    num = heapq.heappop(minhq)
                    numberdict[num] -= 1

    while maxhq and numberdict[-maxhq[0]] <= 0:
        heapq.heappop(maxhq)
    while minhq and numberdict[minhq[0]] <= 0:
        heapq.heappop(minhq)

    if maxhq and minhq:
        answer[0] = -maxhq[0]
        answer[1] = minhq[0]

    return answer


operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))