def solution(dartResult):
    answer = []
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    num = ''
    cnt = 1
    for i in range(len(dartResult)):

        if dartResult[i] in nums:
            num += dartResult[i]
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                bonus = 1
            elif dartResult[i] == 'D':
                bonus = 2
            else:
                bonus = 3

            if i == len(dartResult)-1 or dartResult[i + 1] not in ['*', '#']:
                answer.append(int(num) ** bonus)
                num = ''
                cnt += 1
            else:
                option = dartResult[i + 1]
                if option == '*':
                    if cnt == 1:
                        answer.append(int(num) ** bonus * 2)
                        num = ''
                        cnt += 1
                    else:
                        answer[-1] *= 2
                        answer.append(int(num) ** bonus * 2)
                        num = ''
                        cnt += 1
                else:
                    answer.append(int(num) ** bonus * -1)
                    num = ''
                    cnt += 1

    return sum(answer)