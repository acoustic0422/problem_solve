"""
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057
"""

def solution(s):
    answer = 1000

    length = len(s)

    if length == 1:
        return 1

    for l in range(1,length//2 + 1):
        idx = l
        cand = ""
        temp = s[:l]
        numDup = 1
        while idx < length:
            if s[idx:idx+l] == temp:
                numDup += 1
            else:
                if numDup > 1:
                    cand += str(numDup)
                    numDup = 1
                cand += temp
                temp = s[idx:idx+l]
            idx += l
        if numDup > 1:
            cand += str(numDup)
        cand += temp

        answer = min(len(cand), answer)

    return answer


s = "a"
print(solution(s))
