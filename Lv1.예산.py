def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(len(d)):
        if budget - d[cnt] >= 0:
            budget -= d[cnt]
            cnt += 1
        else:
            break
    return cnt