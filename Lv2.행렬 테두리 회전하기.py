def solution(rows, columns, queries):
    answer = []
    matrix = [[] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            matrix[i].append((i) * columns + (j + 1))

    for query in queries:

        for i in range(4):
            query[i] -= 1

        tmp = matrix[query[0]][query[1]]
        small = matrix[query[0]][query[1]]

        # left
        for i in range(query[0] + 1, query[2] + 1):
            matrix[i - 1][query[1]] = matrix[i][query[1]]
            small = min(small, matrix[i][query[1]])
        # bottom
        for i in range(query[1] + 1, query[3] + 1):
            matrix[query[2]][i - 1] = matrix[query[2]][i]
            small = min(small, matrix[query[2]][i])
        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            matrix[i + 1][query[3]] = matrix[i][query[3]]
            small = min(small, matrix[i][query[3]])
        # top
        for i in range(query[3] - 1, query[1] - 1, -1):
            matrix[query[0]][i + 1] = matrix[query[0]][i]
            small = min(small, matrix[query[0]][i])

        matrix[query[0]][query[1] + 1] = tmp
        answer.append(small)

    return answer