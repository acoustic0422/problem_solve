"""
불량 사용자
https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
"""

answer = 0
ans_set = set()


def check_id(cnt, user_id, banned_id, visited):
    if cnt == len(banned_id):
        temp = []
        for i in range(len(visited)):
            if visited[i] == 1:
                temp.append(user_id[i])
        temp.sort()
        temp = tuple(temp)
        if temp not in ans_set:
            ans_set.add(temp)
        return

    for i in range(len(user_id)):
        if visited[i] == 0 and len(user_id[i]) == len(banned_id[cnt]):
            flag = 0
            for k in range(len(user_id[i])):
                if banned_id[cnt][k] != '*' and user_id[i][k] != banned_id[cnt][k]:
                    flag = 1
                    break
            if flag == 0:
                visited[i] = 1
                check_id(cnt+1, user_id, banned_id, visited)
                visited[i] = 0


def solution(user_id, banned_id):
    global answer

    visited = [0 for _ in range(len(user_id))]
    check_id(0,user_id, banned_id, visited)

    return len(ans_set)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))
