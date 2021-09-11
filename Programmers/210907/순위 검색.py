"""
순위 검색
https://programmers.co.kr/learn/courses/30/lessons/72412
"""

from collections import defaultdict

def solution(info, query):
    answer = []

    infodict = defaultdict(list)
    for i in info:
        i = i.split()
        score = int(i[-1])
        i = i[:-1]

        # 가능한 모든 조합 고려하여 dict에 미리 집어넣음 !! 핵심
        for first in [i[0], '-']:
            for second in [i[1], '-']:
                for third in [i[2], '-']:
                    for fourth in [i[3], '-']:
                        infodict[first+second+third+fourth].append(score)

    # 각각의 List Sort (내림차순)
    for item in infodict:
        infodict[item].sort(reverse=True)

    for q in query:
        q = q.replace('and', '').split()
        score = int(q[-1])
        q = "".join(q[:-1])
        scoreList = infodict[q]

        left = 0
        right = len(scoreList)-1
        base = 0
        # 점수를 넘은 사람이 얼마나 되는지 find (이분탐색)
        while left <= right:
            mid = (left + right) // 2
            if scoreList[mid] >= score:
                base = mid + 1
                left = mid + 1
            else:
                right = mid - 1

        answer.append(base)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))