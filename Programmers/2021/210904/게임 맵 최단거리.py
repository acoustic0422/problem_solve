"""
게임 맵 최단거리
https://programmers.co.kr/learn/courses/30/lessons/1844
"""

from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    visited[0][0] = True
    q.append((0,0,1)) # y,x,len
    while q:
        y,x,way = q.popleft()
        if y == n-1 and x == m-1:
            answer = way
            break
        for dy, dx in delta:
            if 0 <= x+dx < m and 0 <= y+dy < n and maps[y+dy][x+dx] == 1 and visited[y+dy][x+dx] == False:
                visited[y+dy][x+dx] = True
                q.append((y+dy, x+dx, way+1))

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))