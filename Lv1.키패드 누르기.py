def solution(numbers, hand):
    num = [[1, 4, 7], [3, 6, 9], [2, 5, 8, 0]]
    location = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
    result = ''
    left_right = [[location.index('*')//3, location.index('*')%3],
                  [location.index('#')//3, location.index('#')%3]]

    for i in numbers:
        if i in num[0]:
            result += 'L'
            left_right[0] = [location.index(i)//3, location.index(i)%3]
        elif i in num[1]:
            result += 'R'
            left_right[1] = [location.index(i)//3, location.index(i)%3]
        else:
            target_l = abs(location.index(i)//3 - left_right[0][0]) + abs(location.index(i)%3 - left_right[0][1])
            target_r = abs(location.index(i)//3 - left_right[1][0]) + abs(location.index(i)%3 - left_right[1][1])

            if target_l > target_r:
                result += 'R'
                left_right[1] = [location.index(i)//3, location.index(i)%3]
            elif target_r > target_l:
                result += 'L'
                left_right[0] = [location.index(i)//3, location.index(i)%3]
            else:
                if hand == 'right':
                    result += 'R'
                    left_right[1] = [location.index(i)//3, location.index(i)%3]
                else:
                    result += 'L'
                    left_right[0] = [location.index(i)//3, location.index(i)%3]
    return result