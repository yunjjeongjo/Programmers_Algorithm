def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    pattern = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0
    for i in range(a-1):
        date += pattern[i]
    answer = day[(date+b) % 7]

    return answer