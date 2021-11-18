from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    b = deque([0] * bridge_length)
    c = deque(truck_weights)
    while len(b) != 0:
        time += 1
        b.popleft()
        if c:
            if sum(b) + c[0] <= weight:
                b.append(c.popleft())
            else:
                b.append(0)

    return time