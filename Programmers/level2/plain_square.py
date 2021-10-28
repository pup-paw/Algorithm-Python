# def solution(w, h):
#     return sum(int(h * i / w) for i in range(w)) * 2


# print(solution(8, 12))

# import math


# def solution(w, h):
#     a = max(w, h) / min(w, h)
#     return min(w, h) * (max(w, h) - math.ceil(a))

# def solution(w, h):
#     if w == h:
#         a = 1
#     else:
#         a = max(w, h) // min(w, h) + 1
#     return min(w, h) * (max(w, h) - a)

from math import gcd


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


print(solution(8, 12))
