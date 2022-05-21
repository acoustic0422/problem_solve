"""
[카카오 인턴] 보석 쇼핑
https://programmers.co.kr/learn/courses/30/lessons/67258
"""

def check_full(gem_dict):
    for g in gem_dict:
        if gem_dict[g] <= 0:
            return False
    return True

def solution(gems):
    answer = []
    min_len = len(gems)

    gems_set = list(set(gems))
    gems_dict = dict()
    for g in gems_set:
        gems_dict[g] = 0

    left = 0
    right = -1

    while not check_full(gems_dict):
        right += 1
        gems_dict[gems[right]] += 1


    while left <= right < len(gems):
        if gems_dict[gems[left]] == 1:
            if right - left < min_len:
                min_len = right - left
                answer = [left+1, right+1]
            right += 1
            if right > (len(gems) - 1):
                break
            gems_dict[gems[right]] += 1
        elif gems_dict[gems[left]] > 1:
            gems_dict[gems[left]] -= 1
            left += 1

    return answer


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))