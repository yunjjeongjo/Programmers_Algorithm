def solution(name):
    name_alpha = [ord(i) for i in name]
    answer = 0
    min_move = len(name) - 1
    for i in range(len(name_alpha)):
        if name_alpha[i] <= 78:
            answer += name_alpha[i] - 65
        else:
            answer += 90 - name_alpha[i] + 1

        next = i + 1
        while next < len(name) and name_alpha[next] == 65:
            next += 1
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move

    return answer