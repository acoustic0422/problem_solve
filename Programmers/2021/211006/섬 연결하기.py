"""
섬 연결하기
https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3
"""

def find(p,u):
    if u != p[u]:
        p[u] = find(p, p[u])
    return p[u]

def union(p,u,v):
    root1 = find(p,u)
    root2 = find(p,v)
    p[root2] = root1


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2], reverse=True)
    p = [i for i in range(n)]

    numedges = 0

    while True:
        if numedges == n-1:
            break
        u,v,w = costs.pop()
        if find(p,u) != find(p,v):
            union(p,u,v)
            answer += w
            numedges += 1

    return answer


