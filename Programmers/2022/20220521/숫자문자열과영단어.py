def solution(s):
    answer = 0
    numword = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for n in numword:
        s = s.replace(n, numword[n])

    answer = int(s)
    return answer