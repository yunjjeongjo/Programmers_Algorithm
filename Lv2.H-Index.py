def solution(citations):
    answer = 0

    citations.sort()
    max_value = max(citations)
    min_value = min(citations)
    citations_rev = sorted(citations, reverse=True)
    if max_value == min_value:
        return max_value
    else:
        for i in range(max_value, min_value - 1, -1):
            cnt = 0
            for j in citations_rev:
                if j >= i:
                    cnt += 1
                else:
                    break
                answer = max(answer, cnt)
                if i <= cnt:
                    break
    return answer