def solution(rows, columns):
    answer = [[0] * columns for i in range(rows)]
    l = [i for i in range(rows*columns)]
    r, c = 0, 0
    tmp = 1
    while True:
        if l == [] or (rows == columns and tmp == rows*2 + 1):
            break
        answer[r][c] = tmp
        if l.count(r * columns + c) == 1:
            l.remove(r * columns + c)
        if tmp % 2 == 0:
            r = (r + 1) % rows
        else:
            c = (c + 1) % columns
        tmp += 1
    return answer


print(solution(3, 4))
