def solution(record):
    answer = []
    dic = {}

    for line in record:
        split_record = line.split()
        if len(split_record) == 3:
            dic[split_record[1]] = split_record[2]

    for line in record:
        split_record = line.split()

        if split_record[0] == 'Enter':
            enter_message = dic[split_record[1]] + '님이 들어왔습니다.'
            answer.append(enter_message)

        elif split_record[0] == 'Leave':
            leave_message = dic[split_record[1]] + '님이 나갔습니다.'
            answer.append(leave_message)

    return answer