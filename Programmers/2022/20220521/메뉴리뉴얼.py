from itertools import combinations

def calcComb(orders, num, dic):
    for order in orders:
        if len(order) >= num:
            order = ''.join(sorted(list(order)))
            combs = list(combinations(list(order), num))
            for comb in combs:
                c = ''.join(comb)
                if c in dic[num]:
                    dic[num][c] += 1
                else:
                    dic[num][c] = 1

def solution(orders, course):
    answer = []
    menuset = dict()
    for nc in course:
        menuset[nc] = dict()
        calcComb(orders, nc, menuset)
        sortedSet = sorted(menuset[nc].items(), key=lambda x: x[1], reverse=True)
        if len(sortedSet) > 0:
            maxOrder = sortedSet[0][1]
            if maxOrder >= 2:
                for set, numOrder in sortedSet:
                    if numOrder == maxOrder:
                        answer.append(set)
                    else:
                        break
    answer.sort()
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))