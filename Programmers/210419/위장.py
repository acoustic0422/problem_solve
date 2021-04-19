"""
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
"""

def solution(clothes):

    cloth_dict = dict()

    for i in range(len(clothes)):
        _, cat = clothes[i]
        if cat not in cloth_dict:
            cloth_dict[cat] = 1
        else:
            cloth_dict[cat] += 1

    answer = 1
    for num in cloth_dict.values():
        answer *= (num+1)

    return answer-1
