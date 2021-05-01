"""
친구 네트워크
https://www.acmicpc.net/problem/4195
"""

import sys

s = sys.stdin.readline()
T = int(s)


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def union_parent(parent, num_friend, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)

    sum_friends = num_friend[x] + num_friend[y]
    if x < y:
        parent[y] = x
        num_friend[x] = sum_friends
    else:
        parent[x] = y
        num_friend[y] = sum_friends


for tc in range(T):
    s = sys.stdin.readline()
    F = int(s)

    network = []
    idx = 1
    name_dic = dict()
    for i in range(F):
        s = sys.stdin.readline()
        name1, name2 = s.strip().split()
        network.append((name1, name2))
        if name1 not in name_dic:
            name_dic[name1] = idx
            idx += 1
        if name2 not in name_dic:
            name_dic[name2] = idx
            idx += 1

    parent = [i for i in range(idx)]
    num_friend = [1 for i in range(idx)]

    for n1, n2 in network:
        if find_parent(parent, name_dic[n1]) != find_parent(parent, name_dic[n2]):
            union_parent(parent, num_friend, name_dic[n1], name_dic[n2])
        print(num_friend[find_parent(parent, name_dic[n1])])