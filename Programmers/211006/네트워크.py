"""
네트워크
https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
"""

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for num in range(n):
        if visited[num] == False:
            answer += 1
            visited[num] = True
            q = deque()
            q.append(num)

            while q:
                node = q.popleft()
                for i, is_c in enumerate(computers[node]):
                    if node == i:
                        continue
                    else:
                        if is_c == 1 and visited[i] == False:
                            q.append(i)
                            visited[i] = True

    return answer