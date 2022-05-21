"""
다단계 칫솔 판매
https://programmers.co.kr/learn/courses/30/lessons/77486
"""

class node(object):
    def __init__(self, name):
        self.name = name
        self.refer = None
        self.cash = 0

def split_cash(name, enroll_dict, cash):
    if enroll_dict[name].refer == None:
        enroll_dict[name].cash += cash
        return
    else:
        split = int(cash/10)
        mine = cash - split
        enroll_dict[name].cash += mine
        next = enroll_dict[name].refer
        split_cash(next, enroll_dict, split)

def solution(enroll, referral, seller, amount):
    answer = []

    enroll_dict = dict()
    center = node('center')
    enroll_dict['center'] = center
    for en, ref in zip(enroll, referral):
        temp = node(en)
        if ref != '-':
            temp.refer = ref
        else:
            temp.refer = 'center'
        enroll_dict[en] = temp

    for se, am in zip(seller, amount):
        cash = am * 100
        split_cash(se, enroll_dict, cash)

    for en in enroll:
        answer.append(enroll_dict[en].cash)

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
