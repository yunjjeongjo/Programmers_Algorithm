def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]

        temp_array = array[a - 1:b]
        temp_array.sort()

        answer.append(temp_array[c - 1])
    return answer