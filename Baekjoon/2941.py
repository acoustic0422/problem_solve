"""
크로아티아 알파벳
https://www.acmicpc.net/problem/2941
"""

s = input()

cnt = 0
idx = 0
while idx < len(s):
    cnt += 1
    if s[idx] == 'c':
        if idx+1 < len(s):
            if s[idx+1] == '=':
                idx += 1
            elif s[idx+1] == '-':
                idx += 1
    elif s[idx] == 'd':
        if idx + 2 < len(s):
            if s[idx+1] == 'z' and s[idx+2] == '=':
                idx += 2
        if idx + 1 < len(s):
            if s[idx+1] == '-':
                idx += 1
    elif s[idx] == 'l':
        if idx + 1 < len(s):
            if s[idx+1] == 'j':
                idx += 1
    elif s[idx] == 'n':
        if idx + 1 < len(s):
            if s[idx+1] == 'j':
                idx += 1
    elif s[idx] == 's':
        if idx+1 < len(s):
            if s[idx+1] == '=':
                idx += 1
    elif s[idx] == 'z':
        if idx + 1 < len(s):
            if s[idx + 1] == '=':
                idx += 1

    idx += 1

print(cnt)