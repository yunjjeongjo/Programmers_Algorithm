import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        small_1 = heapq.heappop(scoville)

        if small_1 > K:
            break

        small_2 = heapq.heappop(scoville)
        sum = small_1 + small_2 * 2
        heapq.heappush(scoville, sum)
        answer += 1

    last_value = heapq.heappop(scoville)

    if last_value < K:
        answer = -1

    return answer