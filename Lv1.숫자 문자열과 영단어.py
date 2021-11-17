def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    temp = ''

    for i in range(len(s)):
        if s[i].isdigit():
            result += s[i]
        else:
            temp += s[i]
            if temp in words:
                result += str(words.index(temp))
                temp = ''
    print(result)
    answer = int(result)
    return answer