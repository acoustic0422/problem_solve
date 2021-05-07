"""
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3
"""

# 시간초과 코드
# min_friend = 10
#
# def check_complete(weak, visited):
#     for w in weak:
#         if visited[w] == 0:
#             return False
#     return True
#
#
# def find_min(n, cnt, weak, dist, visited):
#     global min_friend
#     if cnt >= min_friend:
#         return
#     if check_complete(weak, visited):
#         if min_friend > cnt:
#             min_friend = cnt
#             return
#     if len(dist) == 0:
#         return
#
#     able = dist.pop()
#     for w in weak:
#         if visited[w] == 0:
#             nvisited = visited[:]
#             l = able + 1
#             now = w
#             for i in range(l):
#                 if i + now >= n:
#                     nvisited[i+now-n] += 1
#                 else:
#                     nvisited[i+now] += 1
#             find_min(n,cnt+1, weak, dist, nvisited)
#     dist.append(able)
#
# def solution(n, weak, dist):
#     global min_friend
#     ld = len(dist)
#     min_friend = ld + 1
#     visited = [0 for _ in range(n)]
#     dist.sort()
#     find_min(n,0,weak, dist, visited)
#
#     if min_friend == ld + 1:
#         return -1
#     else:
#         return min_friend

def solution(n,weak, dist):
    W,F = len(weak), len(dist)
    repair_list = [()] # 현재까지 고칠 수 있는 경우의 수를 저장
    count = 0 # 투입한 친구의 수
    dist.sort(reverse=True) # 움직일 수 있는 거리가 큰 친구부터 확인

    for can_move in dist:
        repairs = [] # 친구별 고칠 수 있는 취약점들 확인
        count += 1

        for i, wp in enumerate(weak): # 각 weak point별로
            start = wp # 시작점은 weak point에서
            ends = weak[i:] + [n + w for w in weak[:i]] # wp에서 갈 수 있는 point를 weak내에서 찾는다.
            # 만일 n-1에서 시작이면 그 후의 weak는 n을 더한것이라고 생각할 수 있다.
            can = [end % n for end in ends if end-start <= can_move]
            # can_move보다 작으면 n으로 나눈 나머지를 적용해 원래 weak_point를 저장한다
            repairs.append(set(can)) # set으로 만들어준다 (중복을제거)

        cand = set() # 후보들을 저장할 set을선언
        for r in repairs: # 현재 친구가 고칠 수 있는 취약점들의 집합을 하나하나 확인하면서,
            for x in repair_list: # 현재까지 고칠수 있는 경우의수를 하나하나 확인한다.
                new = r | set(x) # 기존의 경우의수 + 현재 친구가 고칠수있는 경우의수의 합집합을 만든다
                if len(new) == W: # 만일 합집합의 길이가 모든 취약점의 길이면, 즉, 모두 고칠수 있으면
                    return count # 현재까지 친구 count를 리턴한다
                cand.add(tuple(new)) # 아니면 현재까지 고칠수있는 새로운 경우의수를 tuple로 넣는다
        repair_list = cand # cand를 새로운 현재까지의 경우의수로 둔다

    return -1 # 모든 과정을 거쳐도 다 고치지 못하면 -1 리턴



weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
n = 12

print(solution(n, weak, dist))
