"""
다리 만들기 2
https://www.acmicpc.net/problem/17472
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
N,M = map(int, s.split())

world = []
for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    world.append(line)

visited = [[0 for _ in range(M)] for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M):
        if world[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            world[i][j] = cnt
            while q:
                y, x = q.popleft()
                for dy, dx in delta:
                    if 0 <= x+dx < M and 0 <= y+dy < N and visited[y+dy][x+dx] == 0:
                        if world[y+dy][x+dx] == 1:
                            visited[y+dy][x+dx] = 1
                            world[y+dy][x+dx] = cnt
                            q.append((y+dy, x+dx))
            cnt += 1

edges = [[0 for _ in range(7)] for _ in range(7)]

for i in range(N):
    for j in range(M):
        if world[i][j] != 0:
            now = world[i][j]
            ypos = i
            xpos = j+1
            bridge_len = 0
            ## 오른쪽 방향
            while xpos < M and world[ypos][xpos] != now:
                if world[ypos][xpos] == 0: # 물인경우
                    bridge_len += 1
                    xpos += 1
                elif world[ypos][xpos] == now:
                    break
                elif world[ypos][xpos] != now:
                    if bridge_len >= 2:
                        next = world[ypos][xpos]
                        if edges[now][next] == 0:
                            edges[now][next] = bridge_len
                            edges[next][now] = bridge_len
                        else:
                            if edges[now][next] > bridge_len:
                                edges[now][next] = bridge_len
                                edges[next][now] = bridge_len
                    break
            ## 왼쪽방향
            ypos = i
            xpos = j - 1
            bridge_len = 0
            while xpos >= 0 and world[ypos][xpos] != now:
                if world[ypos][xpos] == 0:
                    bridge_len += 1
                    xpos -= 1
                elif world[ypos][xpos] == now:
                    break
                elif world[ypos][xpos] != now:
                    if bridge_len >= 2:
                        next = world[ypos][xpos]
                        if edges[now][next] == 0:
                            edges[now][next] = bridge_len
                            edges[next][now] = bridge_len
                        else:
                            if edges[now][next] > bridge_len:
                                edges[now][next] = bridge_len
                                edges[next][now] = bridge_len
                    break

            ## 아래방향
            ypos = i + 1
            xpos = j
            bridge_len = 0
            while ypos < N and world[ypos][xpos] != now:
                if world[ypos][xpos] == 0:
                    bridge_len += 1
                    ypos += 1
                elif world[ypos][xpos] == now:
                    break
                elif world[ypos][xpos] != now:
                    if bridge_len >= 2:
                        next = world[ypos][xpos]
                        if edges[now][next] == 0:
                            edges[now][next] = bridge_len
                            edges[next][now] = bridge_len
                        else:
                            if edges[now][next] > bridge_len:
                                edges[now][next] = bridge_len
                                edges[next][now] = bridge_len
                    break

            ## 위방향
            ypos = i - 1
            xpos = j
            bridge_len = 0
            while ypos >= 0 and world[ypos][xpos] != now:
                if world[ypos][xpos] == 0:
                    bridge_len += 1
                    ypos -= 1
                elif world[ypos][xpos] == now:
                    break
                elif world[ypos][xpos] != now:
                    if bridge_len >= 2:
                        next = world[ypos][xpos]
                        if edges[now][next] == 0:
                            edges[now][next] = bridge_len
                            edges[next][now] = bridge_len
                        else:
                            if edges[now][next] > bridge_len:
                                edges[now][next] = bridge_len
                                edges[next][now] = bridge_len
                    break

edge_list = []
for i in range(7):
    for j in range(i,7):
        if edges[i][j] > 0:
            edge_list.append((i,j,edges[i][j]))

edge_list.sort(key = lambda x: x[2])

if len(edge_list) < cnt - 2:
    print(-1)
else:
    result = 0
    edge_cnt = 0
    parent = [i for i in range(7)]

    def Find(a):
        if parent[a] != a:
            parent[a] = Find(parent[a])
        return parent[a]

    def Union(a,b):
        x = Find(a)
        y = Find(b)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    for f,t,w in edge_list:
        if Find(f) != Find(t):
            Union(f,t)
            result += w
            edge_cnt += 1
        if edge_cnt == cnt-2:
            break

    flag = 0
    if edge_cnt < cnt-2:
        flag = 1

    if flag == 1:
        print(-1)
    else:
        print(result)


