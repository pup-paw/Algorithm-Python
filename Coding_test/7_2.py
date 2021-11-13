def solution(grid, clockwise):
    answer = ['' for i in range(len(grid))]
    for g in grid:
        i = (len(g) - 1) // 2
        for word in g:
            answer[len(grid) - 1 - i] = word + answer[len(grid) - 1 - i]
            if len(answer[len(grid) - 1 - i]) % 2 == 1:
                i -= 1
    return answer if clockwise else solution(answer, True)


print(solution(["A", "MAN", "DRINK", "WATER11"], False))
