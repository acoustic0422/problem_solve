"""
스타트와 링크
https://www.acmicpc.net/problem/14889
"""

import sys

s = sys.stdin.readline()
N = int(s)

ability_table = []

for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    ability_table.append(line)

team1 = set()
min_diff = 1000000000

def sum_ability(member):
    result = 0
    for i in range(len(member)):
        for j in range(i+1, len(member)):
            result += ability_table[member[i]][member[j]]
            result += ability_table[member[j]][member[i]]
    return result


def make_team(idx, cnt):
    if cnt == N//2:
        team2 = set()
        for i in range(N):
            if i not in team1:
                team2.add(i)
        t1_ability = sum_ability(list(team1))
        t2_ability = sum_ability(list(team2))
        global min_diff
        if min_diff > abs(t1_ability - t2_ability):
            min_diff = abs(t1_ability - t2_ability)

    for i in range(idx, N):
        if i not in team1:
            team1.add(i)
            make_team(i, cnt+1)
            team1.remove(i)


make_team(0,0)
print(min_diff)
