def solution(n, arr1, arr2):
    answer = []
    map1 = [[0] * n for _ in range(n)]
    for i in range(len(arr1)):
        cnt = 0
        x = arr1[i]
        while x > 0:
            if x % 2 != 0:
                map1[i][n - cnt - 1] = 1
            x = x // 2
            cnt += 1
    for i in range(len(arr2)):
        cnt = 0
        x = arr2[i]
        while x > 0:
            if x % 2 != 0:
                map1[i][n - cnt - 1] = 1
            x = x // 2
            cnt += 1
    for i in map1:
        line = ''
        for j in i:
            if j == 1:
                line += '#'
            else:
                line += ' '
        answer.append(line)

    return answer