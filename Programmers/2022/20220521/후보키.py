from itertools import combinations

def checkDup(result, cand):
    cand = set(cand)
    for r in result:
        r = set(r)
        if r.intersection(cand) == r or r.intersection(cand) == cand:
            return False
    return True

def solution(relation):
    result = []

    col = len(relation[0])
    row = len(relation)

    columns = [n for n in range(col)]

    for nc in range(1, col+1):
        for key in combinations(columns, nc):
            check = set()
            for r in relation:
                temp = ""
                for k in key:
                    temp += r[k]
                check.add(temp)
            if len(check) == row:
                if checkDup(result, key):
                    result.append(key)
    answer = len(result)
    return answer


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))