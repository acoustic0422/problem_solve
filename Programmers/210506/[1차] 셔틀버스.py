"""
[1차] 셔틀버스
https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
"""


def time_string_to_min(time):
    hour, min = time.split(':')
    res = int(hour) * 60 + int(min)
    return res

def solution(n, t, m, timetable):
    answer = ''
    mintable = []
    for time in timetable:
        mintable.append(time_string_to_min(time))
    mintable.sort(reverse=True)

    now = time_string_to_min("09:00")
    while n:
        n -= 1
        bus = []
        while mintable and len(bus) < m and mintable[-1] <= now:
            bus.append(mintable.pop())

        if len(bus) < m:
            latest = now
        else:
            latest = bus[-1] -1

        now += t

    hour = latest // 60
    min = latest % 60

    if hour < 10:
        answer += '0'
        answer += str(hour)
    else:
        answer += str(hour)
    answer += ':'
    if min < 10:
        answer += '0'
        answer += str(min)
    else:
        answer += str(min)

    return answer

timetable = ["09:10", "09:09", "08:00"]
n = 2
t = 10
m = 2
print(solution(n,t,m,timetable))
