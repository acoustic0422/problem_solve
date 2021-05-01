"""
큐빙
https://www.acmicpc.net/problem/5373
"""

import sys
from copy import deepcopy


def turn_face(plane, dir):
    if dir == '+': # 시계
        for _ in range(2):
            temp = plane[0][0]
            px, py = 0,0
            while py < 2:
                plane[py][px] = plane[py+1][px]
                py += 1
            while px < 2:
                plane[py][px] = plane[py][px+1]
                px += 1
            while py > 0:
                plane[py][px] = plane[py-1][px]
                py -= 1
            while px > 0:
                plane[py][px] = plane[py][px-1]
                px -= 1
            plane[0][1] = temp

    else: # 반시계
        for _ in range(2):
            temp = plane[0][0]
            px, py = 0, 0
            while px < 2:
                plane[py][px] = plane[py][px+1]
                px += 1
            while py < 2:
                plane[py][px] = plane[py+1][px]
                py += 1
            while px > 0:
                plane[py][px] = plane[py][px-1]
                px -= 1
            while py > 0:
                plane[py][px] = plane[py-1][px]
                py -= 1
            plane[1][0] = temp


def rotate(cm, cube):
    F = Face[cm[0]]
    d = cm[1]

    turn_face(cube[F], d)
    if F == 0: ## Up
        if d == '+': ## 시계
            temp = cube[Face['B']][0]
            cube[Face['B']][0] = cube[Face['L']][0]
            cube[Face['L']][0] = cube[Face['F']][0]
            cube[Face['F']][0] = cube[Face['R']][0]
            cube[Face['R']][0] = temp
        else:
            temp = cube[Face['B']][0]
            cube[Face['B']][0] = cube[Face['R']][0]
            cube[Face['R']][0] = cube[Face['F']][0]
            cube[Face['F']][0] = cube[Face['L']][0]
            cube[Face['L']][0] = temp
    elif F == 1: ## down
        if d == '+':  ## 시계
            temp = cube[Face['B']][2]
            cube[Face['B']][2] = cube[Face['R']][2]
            cube[Face['R']][2] = cube[Face['F']][2]
            cube[Face['F']][2] = cube[Face['L']][2]
            cube[Face['L']][2] = temp
        else:
            temp = cube[Face['B']][2]
            cube[Face['B']][2] = cube[Face['L']][2]
            cube[Face['L']][2] = cube[Face['F']][2]
            cube[Face['F']][2] = cube[Face['R']][2]
            cube[Face['R']][2] = temp
    elif F == 2: ## Front
        if d == '+': ## 시계
            [a,b,c] = cube[Face['U']][2]
            cube[Face['U']][2] = [cube[Face['L']][2][2], cube[Face['L']][1][2], cube[Face['L']][0][2]]
            [cube[Face['L']][0][2], cube[Face['L']][1][2], cube[Face['L']][2][2]] = cube[Face['D']][0]
            cube[Face['D']][0] = [cube[Face['R']][2][0], cube[Face['R']][1][0], cube[Face['R']][0][0]]
            [cube[Face['R']][0][0], cube[Face['R']][1][0], cube[Face['R']][2][0]] = [a,b,c]
        else:
            [a,b,c] = cube[Face['U']][2]
            cube[Face['U']][2] = [cube[Face['R']][0][0], cube[Face['R']][1][0], cube[Face['R']][2][0]]
            [cube[Face['R']][2][0], cube[Face['R']][1][0], cube[Face['R']][0][0]] = cube[Face['D']][0]
            cube[Face['D']][0] = [cube[Face['L']][0][2], cube[Face['L']][1][2], cube[Face['L']][2][2]]
            [cube[Face['L']][2][2], cube[Face['L']][1][2], cube[Face['L']][0][2]] = [a,b,c]

    elif F == 3: ## Back
        if d == '+': ## 시계
            [a,b,c] = cube[Face['D']][2]
            cube[Face['D']][2] = [cube[Face['L']][0][0], cube[Face['L']][1][0], cube[Face['L']][2][0]]
            [cube[Face['L']][2][0], cube[Face['L']][1][0], cube[Face['L']][0][0]] = cube[Face['U']][0]
            cube[Face['U']][0] = [cube[Face['R']][0][2], cube[Face['R']][1][2], cube[Face['R']][2][2]]
            [cube[Face['R']][2][2], cube[Face['R']][1][2], cube[Face['R']][0][2]] = [a,b,c]
        else:
            [a,b,c] = cube[Face['D']][2]
            cube[Face['D']][2] = [cube[Face['R']][2][2], cube[Face['R']][1][2], cube[Face['R']][0][2]]
            [cube[Face['R']][0][2], cube[Face['R']][1][2], cube[Face['R']][2][2]] = cube[Face['U']][0]
            cube[Face['U']][0] = [cube[Face['L']][2][0], cube[Face['L']][1][0], cube[Face['L']][0][0]]
            [cube[Face['L']][0][0], cube[Face['L']][1][0], cube[Face['L']][2][0]] = [a,b,c]

    elif F == 4: ## Left
        if d == '+': ## 시계
            [a,b,c] = [cube[Face['U']][0][0], cube[Face['U']][1][0], cube[Face['U']][2][0]]
            [cube[Face['U']][0][0], cube[Face['U']][1][0], cube[Face['U']][2][0]] = [cube[Face['B']][2][2], cube[Face['B']][1][2], cube[Face['B']][0][2]]
            [cube[Face['B']][2][2], cube[Face['B']][1][2], cube[Face['B']][0][2]] = [cube[Face['D']][0][0], cube[Face['D']][1][0], cube[Face['D']][2][0]]
            [cube[Face['D']][0][0], cube[Face['D']][1][0], cube[Face['D']][2][0]] = [cube[Face['F']][0][0], cube[Face['F']][1][0], cube[Face['F']][2][0]]
            [cube[Face['F']][0][0], cube[Face['F']][1][0], cube[Face['F']][2][0]] = [a,b,c]
        else:
            [a,b,c] = [cube[Face['U']][0][0], cube[Face['U']][1][0], cube[Face['U']][2][0]]
            [cube[Face['U']][0][0], cube[Face['U']][1][0], cube[Face['U']][2][0]] = [cube[Face['F']][0][0], cube[Face['F']][1][0], cube[Face['F']][2][0]]
            [cube[Face['F']][0][0], cube[Face['F']][1][0], cube[Face['F']][2][0]] = [cube[Face['D']][0][0], cube[Face['D']][1][0], cube[Face['D']][2][0]]
            [cube[Face['D']][0][0], cube[Face['D']][1][0], cube[Face['D']][2][0]] = [cube[Face['B']][2][2], cube[Face['B']][1][2], cube[Face['B']][0][2]]
            [cube[Face['B']][2][2], cube[Face['B']][1][2], cube[Face['B']][0][2]] = [a, b, c]
    elif F == 5: ## Right
        if d == '+':  ## 시계
            [a, b, c] = [cube[Face['U']][0][2], cube[Face['U']][1][2], cube[Face['U']][2][2]]
            [cube[Face['U']][0][2], cube[Face['U']][1][2], cube[Face['U']][2][2]] = [cube[Face['F']][0][2], cube[Face['F']][1][2], cube[Face['F']][2][2]]
            [cube[Face['F']][0][2], cube[Face['F']][1][2], cube[Face['F']][2][2]] = [cube[Face['D']][0][2], cube[Face['D']][1][2], cube[Face['D']][2][2]]
            [cube[Face['D']][0][2], cube[Face['D']][1][2], cube[Face['D']][2][2]] = [cube[Face['B']][2][0], cube[Face['B']][1][0], cube[Face['B']][0][0]]
            [cube[Face['B']][2][0], cube[Face['B']][1][0], cube[Face['B']][0][0]] = [a, b, c]
        else:
            [a, b, c] = cube[Face['U']][0][2], cube[Face['U']][1][2], cube[Face['U']][2][2]
            [cube[Face['U']][0][2], cube[Face['U']][1][2], cube[Face['U']][2][2]] = [cube[Face['B']][2][0], cube[Face['B']][1][0], cube[Face['B']][0][0]]
            [cube[Face['B']][2][0], cube[Face['B']][1][0], cube[Face['B']][0][0]] = [cube[Face['D']][0][2], cube[Face['D']][1][2], cube[Face['D']][2][2]]
            [cube[Face['D']][0][2], cube[Face['D']][1][2], cube[Face['D']][2][2]] = [cube[Face['F']][0][2], cube[Face['F']][1][2], cube[Face['F']][2][2]]
            [cube[Face['F']][0][2], cube[Face['F']][1][2], cube[Face['F']][2][2]] = [a, b, c]


colors = ['w','y','r','o','g','b']
Face = {'U':0, 'D':1, 'F':2, 'B':3, 'L':4, 'R':5}

cube = []
for c in colors:
    plane = []
    for _ in range(3):
        plane.append([c,c,c])
    cube.append(plane)

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    n = int(s)
    s = sys.stdin.readline()
    command = list(s.strip().split())
    rubic = deepcopy(cube)
    for cm in command:
        rotate(cm,rubic)

    for line in rubic[Face['U']]:
        print(''.join(line))

