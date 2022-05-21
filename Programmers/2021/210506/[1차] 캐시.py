"""
[1차] 캐시
https://programmers.co.kr/learn/courses/30/lessons/17680
"""

def solution(cacheSize, cities):
    answer = 0

    cache = dict()

    for c in cities:
        c = c.lower()
        if c not in cache: # MISS
            if len(cache) < cacheSize:
                cache[c] = 0
                answer += 5
            else:
                old_used = -1
                cand = ''
                for k in cache:
                    if cache[k] > old_used:
                        old_used = cache[k]
                        cand = k
                if cand != '':
                    del cache[cand]
                    cache[c] = 0
                answer += 5
        else:
            cache[c] = 0
            answer += 1

        for k in cache:
            cache[k] += 1

    return answer


cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cachesize = 2
print(solution(cachesize, cities))
