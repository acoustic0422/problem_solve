"""
[카카오 인턴] 동굴 탐험
https://programmers.co.kr/learn/courses/30/lessons/67260
** 시간초과... 풀이 봄
"""

# 시간초과 코드
# from collections import deque
#
# def bfs(edges, start, target, order):
#     q = deque()
#     q.append(start)
#     visited = [0 for _ in range(len(edges))]
#     visited[start] = 1
#
#     back_order = set()
#     for o in order:
#         back_order.add(o[-1])
#
#     while q:
#         cnode = q.popleft()
#         for i in edges[cnode]:
#             if i == target:
#                 return True
#             else:
#                 if i not in back_order and visited[i] == 0:
#                     visited[i] = 1
#                     q.append(i)
#
#     return False
#
#
# def solution(n, path, order):
#     answer = True
#
#     edges = [[] for _ in range(n)]
#     for f,t in path:
#         edges[f].append(t)
#         edges[t].append(f)
#
#     flag = 0
#     q = deque()
#     for o in order:
#         q.append(o)
#
#     while q:
#         l = len(q)
#         for _ in range(l):
#             start, target = q.popleft()
#             if bfs(edges, start, target, list(q)):
#                 continue
#             else:
#                 q.append([start, target])
#         if len(q) == l:
#             flag = 1
#             break
#
#     if flag == 1:
#         answer = False
#     else:
#         answer = True
#     return answer

from collections import deque

def solution(n,path,order):
    wait = [0 for _ in range(n)]
    check = [0 for _ in range(n)]
    edges = [[] for _ in range(n)]

    for f,t in path:
        edges[f].append(t)
        edges[t].append(f)

    before = {y:x for x,y in order} # 어떤 노드 방문전에 들러야 하는 방
    after = {x:y for x,y in order} # 어떤 노드 방문 후에 들러야 하는 방

    q = deque()
    q.append(0) # 입구는 0부터이므로, 0 넣는다
    while q:
        ck = q.popleft() # 현재 노드기준
        # if 현재노드 방문전에 들러야 하는 방이 있고,
        # 그 방을 방문하지 않은 상태에서 wait이 아니라면
        # wait처리후 다음 노드를 확인한다.
        if ck in before and check[before[ck]] == 0 and wait[ck] == 0:
            wait[ck] = 1
            continue
        # if 현재노드 방문 후에 들러야 하는 방이 있으면,
        # if 그 방이 현재 wait상태라면
        # 그방을 대기열에 넣는다(그방으로 이동이라 생각하면 될듯)
        elif ck in after:
            if wait[after[ck]]:
                q.append(after[ck])
        # 현재 노드에서 갈수 있는 노드들에 대해서
        # 방문하지 않았다면 대기열에 넣는다
        for nx in edges[ck]:
            if check[nx] == 0:
                q.append(nx)
        # 현재 노드는 방문처리한다.
        check[ck] = 1

    return True if sum(check)==n else False


n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]
print(solution(n,path,order))