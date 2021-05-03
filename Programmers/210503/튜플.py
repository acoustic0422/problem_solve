"""
튜플
https://programmers.co.kr/learn/courses/30/lessons/64065
"""

def solution(s):
    answer = []

    s = s.strip()
    s = s.split('},')

    sets = []
    for c in s:
        c = c.strip('{')
        c = c.strip('}')
        temp = list(map(int,c.split(',')))
        sets.append(temp)
    sets.sort(key=lambda x: len(x))

    ans_set = set()
    for l in sets:
        for num in l:
            if num not in ans_set:
                ans_set.add(num)
                answer.append(num)
                break
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))