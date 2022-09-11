def solution(N, stages):
    k = len(stages)
    failure_rate = {}
    for i in range(1, N + 1):
        cnt = 0
        for j in stages:
            if j == i:
                cnt += 1
        if cnt == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = cnt / k
        k -= cnt
    answer = sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)

    return answer