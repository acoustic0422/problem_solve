"""
단어 변환
https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
"""

from collections import deque
from copy import deepcopy

def wordCompare(w1,w2):
    cnt = 0
    for a,b in zip(w1,w2):
        if a != b:
            cnt += 1
        if cnt > 1:
            return False
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 500
    if target not in words:
        return 0

    visited = set()
    visited.add(begin)
    q = deque()
    q.append((begin, visited, 0))

    while q:
        now, v, cnt = q.popleft()
        if now == target:
            answer = min(answer, cnt)
        if cnt >= answer:
            continue
        for w in words:
            if w not in v:
                if wordCompare(now, w):
                    nv = deepcopy(v)
                    nv.add(w)
                    q.append((w, nv, cnt+1))
    return answer