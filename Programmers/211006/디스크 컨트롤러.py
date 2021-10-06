"""
디스크 컨트롤러
https://programmers.co.kr/learn/courses/30/lessons/42627
"""

import heapq

def solution(jobs):
    answer = 0
    numJobs = len(jobs)
    hq = []
    idx = 0
    time = 0
    jobs.sort(key=lambda x: x[0])
    while hq or idx < numJobs:
        while idx < numJobs and jobs[idx][0] <= time:
            heapq.heappush(hq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if hq:
            dur, s = heapq.heappop(hq)
            answer += time - s + dur
            time += dur
        else:
            time += 1

    return answer // numJobs


jobs = [[0,3],[4,10],[5,2]]
print(solution(jobs))