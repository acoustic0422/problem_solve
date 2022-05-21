"""
복서 정렬하기
https://programmers.co.kr/learn/courses/30/lessons/85002
"""

class Boxer:
    def __init__(self):
        self.winRate = 0
        self.heavyWin = 0
        self.weight = 0
        self.idx = 0

def solution(weights, head2head):
    answer = []

    boxerList = []
    for i, (w, h) in enumerate(zip(weights, head2head)):
        boxer = Boxer()
        boxer.idx = i+1
        boxer.weight = w

        nWin = 0
        nLose = 0
        for p in range(len(h)):
            if h[p] == 'W':
                if weights[p] > w:
                    boxer.heavyWin += 1
                nWin += 1
            elif h[p] == 'L':
                nLose += 1

        if nWin + nLose > 0:
            boxer.winRate = nWin / (nWin+nLose)

        boxerList.append(boxer)

    boxerList.sort(key = lambda x: (x.winRate, x.heavyWin, x.weight, -x.idx), reverse=True)

    for b in boxerList:
        answer.append(b.idx)


    return answer