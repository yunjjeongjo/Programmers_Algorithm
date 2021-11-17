import math
def solution(w,h):
    w, h = max(w, h), min(w, h)
    gcd_num = math.gcd(w, h)
    _w = w // gcd_num
    _h = h // gcd_num

    answer = w*h - (_w+_h-1)*gcd_num


    return answer