import itertools
import math

def solution(nums):
    answer = 0

    nCr = itertools.combinations(nums, 3)
    result = True
    nCr = list(nCr)

    for i in range(len(nCr)):
        sum = 0
        for j in range(3):
            sum += nCr[i][j]
        if prime_number(sum):
            answer += 1
    return answer

def prime_number(x):

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True