from collections import defaultdict
from copy import deepcopy

def split_element(str):
    alpha = "qwertyuioplkjhgfdsazxcvbnm"
    l = len(str)
    str = str.lower()
    strset = defaultdict(int)
    for i in range(l-1):
        if str[i] in alpha and str[i+1] in alpha:
            strset[str[i:i+2]] += 1

    return strset


def solution(str1, str2):
    answer = 0

    str1set = split_element(str1)
    str2set = split_element(str2)

    inter = defaultdict(int)
    union = deepcopy(str2set)

    for k in str1set:
        if k in str2set:
            inter[k] = min(str2set[k], str1set[k])
            union[k] = max(str2set[k], str1set[k])
        else:
            union[k] = str1set[k]

    interlen = 0
    unionlen = 0
    for k in inter:
        interlen += inter[k]
    for k in union:
        unionlen += union[k]

    if unionlen == 0:
        return 65536
    else:
        answer = interlen / unionlen * 65536

    return int(answer)


str1 = "HANDSHAKE"
str2 = "shake hands"
print(solution(str1, str2))