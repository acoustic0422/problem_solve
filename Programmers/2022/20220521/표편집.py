import heapq


def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]

    above = []
    under = [i for i in range(n)]
    heapq.heapify(under)
    trashcan = []

    while k:
        k -= 1
        heapq.heappush(above, -heapq.heappop(under))

    for c in cmd:
        if c[0] == 'D':
            _, cnt = c.split()
            cnt = int(cnt)
            while cnt:
                cnt -= 1
                heapq.heappush(above, -heapq.heappop(under))
        elif c[0] == 'U':
            _, cnt = c.split()
            cnt = int(cnt)
            while cnt:
                cnt -= 1
                heapq.heappush(under, -heapq.heappop(above))
        elif c[0] == 'C':
            trashcan.append(heapq.heappop(under))
            if not under:
                heapq.heappush(under, -heapq.heappop(above))
        elif c[0] == 'Z':
            if trashcan[-1] > under[0]:
                heapq.heappush(under, trashcan.pop())
            else:
                heapq.heappush(above, -trashcan.pop())

    for i in trashcan:
        answer[i] = 'X'

    return "".join(answer)


cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
n = 8
k = 2
print(solution(n,k,cmd))