def solution(grid, clockwise):
    answer = ['' for i in range(len(grid))]
    for g in grid:
        i = (len(g) - 1) // 2
        j = len(grid) - 1
        s = ''
        for word in g:
            if clockwise == 'true':
                index = len(grid) - 1 - i
            else:
                index = j
            if (answer[index]) != '' and s == '':
                s += word
            else:
                s = word + s
                if clockwise == 'true':
                    answer[index] = s + answer[index]
                    i -= 1
                else:
                    answer[index] = answer[index] + s
                    j -= 1
                # else:

                s = ''

    return answer


print(solution(["1", "234", "56789"], "false"))
