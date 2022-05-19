import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
children = [set() for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

test_case = list(map(int, input().split()))

start = 1
q = deque()
q.append(start)
visited[start] = 0

while q:
    x = q.popleft()
    for i in edges[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            children[x].add(i)
            q.append(i)

result = 1

next_index = 1
for i in test_case:
    if next_index == N:
        break
    c_length = len(children[i])
    c1 = set(test_case[next_index: next_index+c_length])
    c2 = children[i]
    if c1 != c2:
        result = 0
        break
    next_index += c_length

print(result)

