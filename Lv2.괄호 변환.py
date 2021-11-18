def func(div):
    cnt_in = 0
    cnt_out = 0
    for i in range(len(div)):
        if div[i] == '(':
            cnt_in += 1
        else:
            cnt_out += 1
        if cnt_in == cnt_out:
            return div[:i + 1], div[i + 1:]


def correct(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True


def solution(p):
    if p == '':
        return ''
    u, v = func(p)

    if correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        new_u = ''

        for i in u[1:len(u)-1]:
            if i == '(':
                new_u += ')'
            else:
                new_u += '('
        answer += new_u
        return answer