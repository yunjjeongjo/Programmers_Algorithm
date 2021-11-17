def solution(new_id):
    new_id = new_id.lower()

    for i in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(i, '')

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    if new_id and new_id[0] == '.':
        new_id = new_id[1:]

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) <= 2:
        last_char = new_id[-1]
        while len(new_id) < 3:
            new_id += last_char

    answer = new_id
    return answer