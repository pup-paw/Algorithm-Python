def solution(grid, clockwise):
    answer = ['' for i in range(len(grid))]
    for g in grid:
        i = (len(g) - 1) // 2
        s = ''
        for word in g:
            if (answer[len(grid) - 1 - i]) != '' and s == '':
                s += word
            else:
                s = word + s
                answer[len(grid) - 1 - i] = s + answer[len(grid) - 1 - i]
                i -= 1
                s = ''
    return answer if clockwise else solution(answer, 'true')


print(solution(["1", "234", "56789"], 'true'))
