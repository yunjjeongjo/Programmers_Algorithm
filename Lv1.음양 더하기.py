def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
            print(answer)
        else:
            answer -= absolutes[i]
            print(answer)

    return answer