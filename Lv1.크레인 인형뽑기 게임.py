def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stack) > 1:
                    value_1 = stack.pop()
                    value_2 = stack.pop()
                    if not value_1 == value_2:
                        stack.append(value_2)
                        stack.append(value_1)
                    else:
                        answer += 2
                break

    return answer