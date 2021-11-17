def solution(lottos, win_nums):
    cnt_zero = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0

    for i in win_nums:
        if i in lottos:
            cnt += 1

    answer = []
    answer.append(rank[cnt + cnt_zero])
    answer.append(rank[cnt])

    return answer