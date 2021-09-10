"""
무지의 먹방 라이브
https://programmers.co.kr/learn/courses/30/lessons/42891
"""

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foodWithIndex = []
    for i, f in enumerate(food_times):
        foodWithIndex.append((f,i+1))
    heapq.heapify(foodWithIndex)

    cumulated = 0
    amount = 0
    while True:
        food, idx = heapq.heappop(foodWithIndex)
        if food <= cumulated:
            continue
        else:
            if (food - cumulated) * (len(foodWithIndex)+1) + amount < k:
                amount += (food - cumulated) * (len(foodWithIndex)+1)
                cumulated = food
            else:
                foodWithIndex.append((food, idx))
                foodWithIndex.sort(key=lambda x: x[1])
                result = (k - amount) % len(foodWithIndex)
                answer = foodWithIndex[result][1]
                break

    return answer

