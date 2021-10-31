def solution(sizes):
    # w = 0
    # h = 0
    # for x, y in sizes:
    #     w = max(w, max(x, y))
    #     h = max(h, min(x, y))
    # return w*h
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
