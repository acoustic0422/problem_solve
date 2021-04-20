"""
자동완성
https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.count = 1

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head

        for ch in string:
            if ch not in curr.child:
                curr.child[ch] = Node(ch)
            else:
                curr.child[ch].count += 1
            curr = curr.child[ch]

    def search(self, string):
        curr = self.head

        cnt = 0
        for ch in string:
            cnt += 1
            if curr.child[ch].count != 1:
                curr = curr.child[ch]
            else:
                break

        return cnt


def solution(words):
    answer = 0

    trie = Trie()
    for w in words:
        trie.insert(w)

    for w in words:
        answer += trie.search(w)

    return answer
