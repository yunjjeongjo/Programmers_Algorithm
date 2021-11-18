def solution(left, right):
    nums = [i for i in range(left, right+1)]
    answer = 0
    a=[]
    for i in range(left, right+1):
        flag = 0
        cnt = 0
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                cnt += 1
                if j == (i//j):
                    flag += 1
        a.append(cnt*2 - flag)
    for i in range(len(a)):
        if a[i] % 2 == 0:
            answer += nums[i]
        else:
            answer -= nums[i]
    return answer