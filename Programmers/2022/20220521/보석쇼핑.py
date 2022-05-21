from collections import defaultdict
def solution(gems):
    answer = []
    linelength = len(gems) + 1
    gemset = set(gems)
    line = defaultdict(int)

    left = 0
    right = 0
    line[gems[right]] += 1
    while left <= right <= len(gems):
        if len(line) < len(gemset):
            right += 1
            if right < len(gems):
                line[gems[right]] += 1
        else:
            length = right - left + 1
            if linelength > length:
                answer = [left+1, right+1]
                linelength = length
            line[gems[left]] -= 1
            if line[gems[left]] == 0:
                del line[gems[left]]
            left += 1

    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))