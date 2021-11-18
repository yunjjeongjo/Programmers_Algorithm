def solution(priorities, location):
    documents = [i for i in range(len(priorities))]
    answer = []
    print(documents)
    while priorities:
        value = priorities.pop(0)
        docu = documents.pop(0)
        print(priorities)
        flag = True
        for i in priorities:
            if i > value:
                priorities.append(value)
                documents.append(docu)
                flag = False
                break
        if flag:
            answer.append(docu)
    result = answer.index(location) + 1
    return result