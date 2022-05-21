"""
후보키
https://programmers.co.kr/learn/courses/30/lessons/42890
"""
answer = 0
ans_comb = []

def check_tuple(relation, comb):
    check = set()
    for col in relation:
        temp = ''
        for i in comb:
            temp += col[i]
        if temp not in check:
            check.add(temp)
        else:
            return False
    return True


def find(cnt, n, idx, comb, relation, visited):
    if cnt == n:
        if check_tuple(relation, comb):
            global ans_comb
            res = set(comb)
            flag = 0
            for ac in ans_comb:
                if res.intersection(ac) == ac:
                    flag = 1
                    break
            if flag == 0:
                ans_comb.append(res)
            return

    for i in range(idx, len(relation[0])):
        if visited[i] == 0:
            visited[i] = 1
            find(cnt+1, n, i+1, comb+[i], relation, visited)
            visited[i] = 0


def solution(relation):
    global answer, ans_comb

    visited = [0 for _ in range(10)]
    for cnt in range(1,len(relation[0])+1):
        find(0, cnt, 0, [], relation,visited)

    print(ans_comb)
    answer = len(ans_comb)
    return answer


relation = [["10", "r", "ma", "2", "41"],
            ["20", "a", "ma", "2", "42"],
            ["30", "a", "co", "3", "41"],
            ["40", "c", "co", "4", "41"],
            ["50", "m", "mu", "3", "41"],
            ["60", "a", "mu", "2", "41"]]

print(solution(relation))
