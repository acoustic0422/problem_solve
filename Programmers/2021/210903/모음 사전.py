"""
모음 사전
https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3
"""

def solution(word):
    vowel = "AEIOU"
    cases = []
    for a in vowel:
        for b in vowel+" ":
            if b == ' ':
                case = a
                cases.append(case)
            else:
                for c in vowel+" ":
                    if c == ' ':
                        case = a+b
                        cases.append(case)
                    else:
                        for d in vowel+" ":
                            if d == ' ':
                                case = a+b+c
                                cases.append(case)
                            else:
                                for e in vowel+" ":
                                    if e == ' ':
                                        case = a+b+c+d
                                        cases.append(case)
                                    else:
                                        case = a+b+c+d+e
                                        cases.append(case)
    cases.sort()
    answer = cases.index(word) + 1
    return answer


word = "EIO"
print(solution(word))