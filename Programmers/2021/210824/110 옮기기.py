"""
110 옮기기
https://programmers.co.kr/learn/courses/30/lessons/77886
"""

def solution(s):
    answer = []
    for w in s:
        num = 0
        word = ""
        for i in range(len(w)):
            if w[i] == '0' and word[-2:] == '11':
                word = word[:-2]
                num += 1
            else:
                word += w[i]

        idx = word.find('11')
        if idx != -1:
            word = word[:idx] + '110'*num + word[idx:]
        else:
            idx2 = word.rfind('0')
            word = word[:idx2+1] + '110'*num + word[idx2+1:]

        answer.append(word)
    return answer


s = ["1100","100111100","0111111010"]
print(solution(s))