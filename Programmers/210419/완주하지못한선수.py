"""
완주하지못한선수
https://programmers.co.kr/learn/courses/30/lessons/42576
"""

from collections import defaultdict

def solution(participant, completion):
    answer = ''
    part_dict = defaultdict(int)

    for p in participant:
        part_dict[p] += 1

    for c in completion:
        part_dict[c] -= 1

    for k,v in part_dict.items():
        if v == 1:
            answer = k
            break

    return answer


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

print(solution(p,c))