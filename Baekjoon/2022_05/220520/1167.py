import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    line = list(map(int, input().split()))
    node = line[0]
    n = 1
    while True:
        edge = line[n:n+2]
        if edge[0] == -1:
            break
        c , wei = edge
        graph[node].append([c,wei])
        n += 2


def dfs(x,wei,distance):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei+b, distance)


distance = [-1 for _ in range(V+1)]
distance[1] = 0

dfs(1,0,distance)

start = distance.index(max(distance))

distance = [-1 for _ in range(V+1)]
distance[start] = 0
dfs(start, 0, distance)

print(max(distance))