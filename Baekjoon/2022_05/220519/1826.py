import sys
import heapq

input = sys.stdin.readline

N = int(input())
fuel = []
# a 주유소까지의 거리, b 채울 수 있는 연료의 양
for _ in range(N):
    a, b = map(int, input().split())
    fuel.append((a,b))

# P = 연료의 양
# L = 주유소까지의 거리
L, P = map(int, input().split())

cnt = 0
heap = []
heapq.heapify(fuel)


while P<L: # 연료양이 주유소까지의 거리보다 작을동안
    # 현재 연료로 갈 수 있는 모든 주유소 확인
    while fuel and fuel[0][0] <= P:
        a, b = heapq.heappop(fuel)
        heapq.heappush(heap, (-b,a)) # 채울 수 있는 연료의 양 max_heap으로 넣는다

    #  갈 수 있는 주유소가 없으면 -1 리턴
    if not heap:
        cnt = -1
        break
    # 갈 수 있는 주유소 중에 제일 많이 충전 가능한 주유소 선택
    b, a = heapq.heappop(heap)
    P += -b # 현재 연료량 증가
    cnt += 1 # 방문횟수 증가가

print(cnt)