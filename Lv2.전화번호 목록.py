def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        a = phone_book[i]
        if a == phone_book[i + 1][0:len(a)]:
            answer = False
            break

    return answer