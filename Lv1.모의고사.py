def solution(answers):
    answer = []
    a = [[1, 2, 3, 4, 5]
        , [2, 1, 2, 3, 2, 4, 2, 5]
        , [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    result = [0 for _ in range(3)]

    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == a[i][j % len(a[i])]:
                result[i] += 1
    print(result)
    max_value = max(result)
    for i in range(len(result)):
        if result[i] == max_value:
            answer.append(i + 1)
    return answer