def solution(nums):
    set_nums = set(nums)
    length = len(nums)//2
    if len(set_nums)>=length:
        answer = length
    else:
        answer = len(set_nums)
    return answer