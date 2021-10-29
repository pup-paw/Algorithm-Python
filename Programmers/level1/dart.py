def solution(dartResult):
    dartResult = dartResult.replace('10', 'x')
    dart = ['10' if x == 'x' else x for x in dartResult]
    point = list()

    i = -1
    sdt = ['S', 'D', 'T']
    for x in dart:
        if x in sdt:
            point[i] **= sdt.index(x) + 1
        elif x == '*':
            if i != 0:
                point[i-1] *= 2
            point[i] *= 2
        elif x == '#':
            point[i] *= -1
        else:
            point.append(int(x))
            i += 1
    return sum(point)


print(solution("10S*2T*3S"))
