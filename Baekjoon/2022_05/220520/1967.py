import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())

graph = [[] for _ in range(N+1)]


def dfs(x, wei, distance):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei+b
            dfs(a, wei+b, distance)


for _ in range(N-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


distance = [-1] * (N+1)
distance[1] = 0

dfs(1,0, distance)

start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
dfs(start, 0, distance)

print(max(distance))