import itertools
import math


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):

            if x % i == 0:
                return False
        return True


def solution(numbers):
    num_list = []
    nPr = [[] for _ in range(len(numbers))]
    answer = 0

    for i in range(len(numbers)):
        num_list.append(numbers[i])

    for i in range(len(num_list)):
        nPr[i] = list(map(''.join, itertools.permutations(num_list, i + 1)))

    for i in range(len(nPr)):
        for j in range(len(nPr[i])):
            nPr[i][j] = int(nPr[i][j])

    nPr = list(itertools.chain.from_iterable(nPr))
    nPr = set(nPr)

    for i in nPr:
        if is_prime_number(i):
            answer += 1

    return answer