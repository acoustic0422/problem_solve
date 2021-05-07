"""
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057
"""

def solution(s):
    answer = 0
    max_part = len(s) // 2
    min_len = len(s)

    for l in range(1,max_part+1):
        idx = 0
        cnt = 1
        temp = ''
        res = ''
        while idx < len(s):
            if temp == '':
                temp = s[idx:idx+l]
            else:
                if s[idx:idx+l] == temp:
                    cnt += 1
                else:
                    if cnt >= 2:
                        res += str(cnt)
                    cnt = 1
                    res += temp
                    temp = s[idx:idx+l]
            idx += l

        if cnt >= 2:
            res += str(cnt)
        cnt = 1
        res += temp

        if min_len > len(res):
            min_len = len(res)
    return min_len


s = "ababcdcdababcdcd"
print(solution(s))