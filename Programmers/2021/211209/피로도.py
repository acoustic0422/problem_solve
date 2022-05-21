"""
피로도
https://programmers.co.kr/learn/courses/30/lessons/87946
"""

from collections import deque
from copy import deepcopy

def solution(k, dungeons):
    answer = 0

    q = deque()
    visited = [False for _ in range(len(dungeons))]

    for i, (mf, uf) in enumerate(dungeons):
        if k >= mf:
            visited[i] = True
            q.append((1, k-uf, deepcopy(visited)))
            visited[i] = False

    while q:
        numd, rf, v = q.popleft()
        if numd > answer:
            answer = numd

        for i in range(len(dungeons)):
            if not v[i] and dungeons[i][0] <= rf:
                v[i] = True
                q.append((numd+1, rf-dungeons[i][1], deepcopy(v)))
                v[i] = False

    return answer


k = 80
d = [[80,20],[50,40],[30,10]]

print(solution(k,d))