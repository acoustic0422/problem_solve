"""
상호 평가
https://programmers.co.kr/learn/courses/30/lessons/83201
"""

def grade(score):
    if score >= 90:
        return 'A'
    elif 80<= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 50 <= score < 70:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    l = len(scores)

    for j in range(l):
        is_max = True
        is_min = True
        avg_score = 0
        for i in range(l):
            avg_score += scores[i][j]
            if i != j:
                if scores[i][j] <= scores[j][j]:
                    is_min = False
                if scores[i][j] >= scores[j][j]:
                    is_max = False
        if is_min or is_max:
            avg_score -= scores[j][j]
            avg_score /= (l-1)
        else:
            avg_score /= l
        answer += grade(avg_score)

    return answer

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))