from collections import  defaultdict
def solution(N, stages):
    answer = []
    numUser = len(stages)
    arriveStage = defaultdict(int)
    failRate = []
    for s in stages:
        arriveStage[s] += 1

    for i in range(1,N+1):
        if numUser > 0:
            rate = arriveStage[i] / numUser
        else:
            rate = 0
        failRate.append((i, rate))
        numUser -= arriveStage[i]

    failRate.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    for f in failRate:
        answer.append(f[0])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))