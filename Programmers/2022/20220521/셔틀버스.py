import heapq

def hour2min(h):
    hour, min = h.split(':')
    return int(hour)*60 + int(min)


def min2hour(m):
    hour = m // 60
    min = m % 60
    result = ""
    if hour < 10:
        result += '0'
    result += str(hour)
    result += ':'
    if min < 10:
        result += '0'
    result += str(min)
    return result


def solution(n, t, m, timetable):
    answer = ''
    timemin = []
    crew = []
    for time in timetable:
        timemin.append(hour2min(time))
    heapq.heapify(timemin)

    bustime = hour2min("09:00")
    while n > 0:
        n -= 1
        while timemin and bustime >= timemin[0]:
            temp = heapq.heappop(timemin)
            heapq.heappush(crew, -temp)

        if len(crew) < m:
            answer = min2hour(bustime)
        else:
            while len(crew) > m:
                temp = heapq.heappop(crew)
                heapq.heappush(timemin, -temp)
            answer = min2hour(-crew[0]-1)
        bustime += t
        crew = []

    return answer


timetable = ["09:10", "09:09", "08:00"]
n = 2
t = 10
m = 2

print(solution(n,t,m,timetable))