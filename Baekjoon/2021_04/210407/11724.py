"""
연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""
import sys

s = sys.stdin.readline()
N,M = map(int, s.split())

dic = dict()
for i in range(N):
    dic[i+1] = []

for i in range(M):
    s = sys.stdin.readline()
    f, t = map(int, s.split())
    dic[f].append(t)
    dic[t].append(f)

visited = set()
cnt = 0
stack = []


for i in range(N):
    if i+1 not in visited:
        visited.add(i+1)
        cnt += 1
        stack.append(i+1)
        while len(stack) > 0:
            curr = stack[-1]
            stack.pop()
            for node in dic[curr]:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)

print(cnt)
