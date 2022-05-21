def solution(gems):
    from collections import defaultdict
    answer = []

    gem_dict = defaultdict(int)

    min_length = 100001

    base_gem = set(gems)
    start = 0
    end = 0
    for idx, g in enumerate(gems):
        if start == 0:
            start = idx+1
        gem_dict[g] += 1
        if len(gem_dict) == len(base_gem):
            end = idx+1
            while gem_dict[gems[start-1]] > 1:
                gem_dict[gems[start-1]] -= 1
                if gem_dict[gems[start-1]] == 0:
                    del gem_dict[gems[start-1]]
                start += 1
            length = end - start + 1
            if length < min_length:
                min_length = length
                answer = [start, end]

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))