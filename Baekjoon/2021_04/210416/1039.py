"""
교환
https://www.acmicpc.net/problem/1039
"""

import sys
from collections import deque

s = sys.stdin.readline()
N,K = map(int, s.split())

q = deque()
q.append(N)
visited = set()
visited.add((N,0))

max_result = -1

if N < 10:
    print(-1)
else:
    cnt = 0
    while q:
        cnt += 1
        if cnt > K:
            l = len(q)
            for _ in range(l):
                num = q.popleft()
                if max_result < num:
                    max_result = num
        else:
            l = len(q)
            for _ in range(l):
                num = q.popleft()
                num_list = list(str(num))

                for i in range(len(num_list)):
                    for j in range(i+1, len(num_list)):
                        num_list[i], num_list[j] = num_list[j], num_list[i]
                        if num_list[0] != '0':
                            next = int("".join(num_list))
                            if (next, cnt) not in visited:
                                visited.add((next,cnt))
                                q.append(next)
                        num_list[i], num_list[j] = num_list[j], num_list[i]

    print(max_result)