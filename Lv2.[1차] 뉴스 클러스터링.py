def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    multi1 = []
    multi2 = []

    for i in range(0, len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            multi1.append(str1[i] + str1[i + 1])
    for i in range(0, len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            multi2.append(str2[i] + str2[i + 1])

    if len(multi1) == 0 and len(multi2) == 0:
        return 65536
    else:

        if len(multi1) >= len(multi2):
            length1 = len(multi1)
            length2 = len(multi2)
            intersection = 0
            for i in range(len(multi2)):
                if multi2[i] in multi1:
                    multi1.remove(multi2[i])
                    intersection += 1

            union = length1 + length2 - intersection

        else:
            length1 = len(multi1)
            length2 = len(multi2)
            intersection = 0
            for i in range(len(multi1)):
                if multi1[i] in multi2:
                    multi2.remove(multi1[i])
                    intersection += 1
            union = length1 + length2 - intersection
        print(union, intersection)
        answer = int(intersection / union * 65536)
    return answer