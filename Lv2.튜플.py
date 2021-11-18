def solution(s):
    answer = []

    s = s.replace('{{', '')
    s = s.replace('}}', '')
    s = s.replace('},{', ' ')
    s = s.split()

    for i in range(len(s)):
        s[i] = s[i].replace(',', ' ')
        s[i] = s[i].split()
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])

    s.sort(key=len)

    answer.append(s[0][0])

    for i in range(1, len(s)):
        for j in s[i]:
            if j not in answer:
                answer.append(j)

    return answer