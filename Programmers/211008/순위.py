"""
순위
https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
"""

from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    winedges = defaultdict(list)
    loseedges = defaultdict(list)

    for w,l in results:
        winedges[w].append(l)
        loseedges[l].append(w)

    for i in range(1, n+1):
        q = deque()
        q.append(i)
        winlosesum = 0
        visited = [False for _ in range(n+1)]
        while q:
            now = q.popleft()
            for nn in winedges[now]:
                if not visited[nn]:
                    visited[nn] = True
                    q.append(nn)
                    winlosesum += 1
        q = deque()
        q.append(i)
        visited = [False for _ in range(n+1)]
        while q:
            now = q.popleft()
            for nn in loseedges[now]:
                if not visited[nn]:
                    visited[nn] = True
                    q.append(nn)
                    winlosesum += 1

        if winlosesum == n - 1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
