"""
텀 프로젝트
https://www.acmicpc.net/problem/9466
"""

import sys

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    N = int(s)
    s = sys.stdin.readline()
    selected = list(map(int, s.split()))

    visited = set()
    saw = set()

    for idx, node in enumerate(selected):
        if (idx+1) not in saw:
            stack = []
            select_v = set()
            curr = idx+1
            stack.append(curr)
            select_v.add(curr)
            while True:
                if selected[curr-1] in saw:
                    while stack:
                        student = stack.pop()
                        saw.add(student)
                    break
                elif selected[curr-1] not in select_v:
                    select_v.add(selected[curr-1])
                    curr = selected[curr-1]
                    stack.append(curr)
                elif selected[curr-1] in select_v:
                    start = selected[curr-1]
                    while stack:
                        student = stack.pop()
                        saw.add(student)
                        visited.add(student)
                        if student == start:
                            break
                    while stack:
                        student = stack.pop()
                        saw.add(student)
                    break

    print(N - len(visited))