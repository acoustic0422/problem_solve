"""
[1차] 뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677
"""

import copy

def solution(str1, str2):
    answer = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    str1 = str1.lower()
    str2 = str2.lower()

    str1_set = dict()
    str2_set = dict()

    for i in range(len(str1)-1):
        temp = ''
        if str1[i] not in alpha:
            continue
        elif str1[i+1] not in alpha:
            continue
        temp += str1[i]
        temp += str1[i+1]

        if temp in str1_set:
            str1_set[temp] += 1
        else:
            str1_set[temp] = 1

    for i in range(len(str2)-1):
        temp = ''
        if str2[i] not in alpha:
            continue
        elif str2[i+1] not in alpha:
            continue
        temp += str2[i]
        temp += str2[i+1]
        if temp in str2_set:
            str2_set[temp] += 1
        else:
            str2_set[temp] = 1

    inter = dict()
    union = copy.deepcopy(str2_set)

    for k in str1_set:
        if k in str2_set:
            temp = min(str2_set[k], str1_set[k])
            inter[k] = temp
    for k in str1_set:
        if k in str2_set:
            temp = max(str1_set[k], str2_set[k])
            union[k] = temp
        else:
            union[k] = str1_set[k]

    inter_len = 0
    union_len = 0
    for k in inter:
        inter_len += inter[k]
    for k in union:
        union_len += union[k]

    if union_len == 0:
        return 65536
    else:
        answer = int( inter_len / union_len * 65536)

    return answer

str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2))