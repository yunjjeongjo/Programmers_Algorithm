import operator


def solution(number, k):
    answer = ''
    number = list(number)
    temp = []

    for i in number:
        while temp and i > temp[-1]:
            if k > 0:
                temp.pop()
                k -= 1
            else:
                break
        temp.append(i)
        print(temp)

    if k > 0:
        for i in range(k):
            temp.pop()

    answer = "".join(temp)
    return answer