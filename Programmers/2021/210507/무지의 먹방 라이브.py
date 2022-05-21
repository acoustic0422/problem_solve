"""
무지의 먹방 라이브
https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
"""

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))

    cnt = 0
    amount = 0
    while k - cnt >= 0:
        food, idx = heap[0]
        if (k - cnt) >= (food- amount) * (len(heap)):
            cnt += (food - amount) * (len(heap))
            heapq.heappop(heap)
            amount = food
        else:
            nom = (k-cnt) // len(heap)
            cnt += nom * (len(heap))
            break

    remain = []
    while heap:
        remain.append(heapq.heappop(heap))
    remain.sort(key= lambda x:x[1])

    answer = remain[k-cnt][1]

    return answer

food_times = [1,2,3,4,5,1,2,3,4,5]
k = 29
print(solution(food_times, k))
