def solution(numbers):
    answer = -1
    ans = 0

    num = [0 for _ in range(10)]

    for i in range(len(numbers)):
        num[numbers[i]] = 1

    for i in range(len(num)):
        if num[i] == 0:
            ans += i

    if ans:
        answer = ans

    return answer