def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        cnt = 1
        pos = 0
        temp = ""
        while pos < len(s):
            if s[pos:pos+i] == s[pos+i:pos+i+i]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt)
                temp += s[pos:pos+i]
                cnt = 1
            pos += i
        answer = min(len(temp), answer)

    return answer

print(solution("abcabcabcabcdededededede"))