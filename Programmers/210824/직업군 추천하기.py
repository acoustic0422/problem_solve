"""
직업군 추천하기
https://programmers.co.kr/learn/courses/30/lessons/84325
"""

def solution(table, languages, preference):
    answer = ''
    table_dict = dict()
    for job in table:
        job_score = list(job.split(' '))
        table_dict[job_score[0]] = dict()
        rate = 5
        for language in job_score[1:]:
            table_dict[job_score[0]][language] = rate
            rate -= 1

    result = []

    for job in table_dict:
        total_score = 0
        for lang, pref in zip(languages, preference):
            if lang in table_dict[job]:
                total_score += table_dict[job][lang] * pref
        result.append((job, total_score))

    result.sort(key= lambda x: (-x[1],x[0]))
    answer = result[0][0]
    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))