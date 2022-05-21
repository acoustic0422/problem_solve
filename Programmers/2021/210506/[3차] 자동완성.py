"""
[3차] 자동완성
https://programmers.co.kr/learn/courses/30/lessons/17685
"""

class node(object):
    def __init__(self):
        self.count = 0
        self.next = dict()

class Trie(object):
    def __init__(self):
        self.root = node()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c in curr.next:
                curr = curr.next[c]
                curr.count += 1
            else:
                curr.next[c] = node()
                curr = curr.next[c]
                curr.count += 1

    def search(self, word):
        curr = self.root
        typing = 0
        for c in word:
            if curr.next[c].count > 1:
                typing += 1
                curr = curr.next[c]
            else:
                typing += 1
                break
        return typing


def solution(words):
    answer = 0

    trie = Trie()

    for w in words:
        trie.insert(w)

    for w in words:
        answer += trie.search(w)

    return answer

words = ["go","gone","guild"]
print(solution(words))
