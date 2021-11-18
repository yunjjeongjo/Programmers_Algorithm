from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            combination = combinations(sorted(order), i)
            temp += combination

        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            for j in counter:
                if counter[j] == max(counter.values()):
                    answer.append(''.join(j))
    return sorted(answer)