"""
전력망을 둘로 나누기
https://programmers.co.kr/learn/courses/30/lessons/86971
"""

from collections import defaultdict, deque

def countNode(n, wiredict):
    cnt = 1
    visited = [False for _ in range(n+1)]
    visited[1] = True
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for next in wiredict[node]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)

    return cnt


def solution(n, wires):
    answer = n
    wiredict = defaultdict(list)
    for a, b in wires:
        wiredict[a].append(b)
        wiredict[b].append(a)

    for a,b in wires:
        wiredict[a].remove(b)
        wiredict[b].remove(a)

        cnt = countNode(n, wiredict)
        answer = min(answer, abs(n - (2 * cnt)))

        wiredict[a].append(b)
        wiredict[b].append(a)

    return answer


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))