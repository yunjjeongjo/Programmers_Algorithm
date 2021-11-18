from itertools import permutations


def calc(op, seq, expression):
    if expression.isdigit():
        return str(expression)
    else:
        if op[seq] == '*':
            exp_split = expression.split('*')
            temp = []
            for i in exp_split:
                temp.append(calc(op, seq + 1, i))
            return str(eval("*".join(temp)))

        elif op[seq] == "+":
            exp_split = expression.split("+")
            temp = []
            for i in exp_split:
                temp.append(calc(op, seq + 1, i))
            return str(eval("+".join(temp)))

        else:
            exp_split = expression.split("-")
            temp = []
            for i in exp_split:
                temp.append(calc(op, seq + 1, i))
            return str(eval("-".join(temp)))


def solution(expression):
    answer = 0
    operators = ['*', '+', '-']
    operations = list(permutations(operators, 3))

    for op in operations:
        result = abs(int(calc(op, 0, expression)))
        answer = max(result, answer)

    return answer