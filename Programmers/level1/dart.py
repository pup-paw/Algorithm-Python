def solution(dartResult):
    answer = [0]
    l = list()
    j = 0
    for i, x in enumerate(dartResult[:]):
        if len(l) == 2:
            l.append(dartResult[j:])
            break
        if i != 0 and 47 < ord(x) < 58:
            if not(47 < ord(dartResult[i-1]) < 58):
                l.append(dartResult[j:i])
                j = i
    print(l)
    for i, x in enumerate(l):
        n = 0
        for k, y in enumerate(x):
            if 47 < ord(y) < 58:
                if 47 < ord(x[k-1]) < 58:
                    n = n*10 + int(y)
                else:
                    n = int(y)
            elif y == 'S':
                n **= 1
            elif y == 'D':
                n **= 2
            elif y == 'T':
                n **= 3
            elif y == '*':
                answer[i] *= 2
                n *= 2
            elif y == '#':
                n *= -1
        answer.append(n)

    return sum(answer)


print(solution("10S*2T*3S"))
