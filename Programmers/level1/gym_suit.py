def solution(n, lost, reserve):
    l = list(set(lost) - set(reserve))
    r = list(set(reserve) - set(lost))
    for x in sorted(l[:]):
        for y in sorted(r):
            if y + 1 == x or y - 1 == x:
                l.remove(x)
                r.remove(y)
                break
    return n - len(l)


print(solution(3, [1, 2], [2, 3]))
