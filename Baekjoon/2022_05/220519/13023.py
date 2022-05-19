import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
visited = [False] * N
result = False

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(depth, x):
    global result

    if depth == 4:
        result = True
        return

    for i in edges[x]:
        if not visited[i] and not result:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if result:
        break

if result:
    print('1')
else:
    print('0')
