def solution(s):
    length = []
    n = len(s)
    result = ""
    if len(s) == 1:
        return 1
    for i in range(1, n // 2 + 1):  # 1~n//2개 단위로 잘라 압축
        cnt = 1
        temp = s[:i]
        for j in range(i, n, i):
            if temp == s[j:j + i]:  # 압축 가능
                cnt += 1
            else:  # 압축 불가능
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + temp
                temp = s[j:j + i]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + temp
        length.append(len(result))
        result = ""

    answer = min(length)
    return answer