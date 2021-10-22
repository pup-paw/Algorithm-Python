def solution(board, moves):
    basket = [0]
    answer = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if basket[-1] == b[m-1]:
                    basket.pop();
                    answer += 2
                else:
                    basket.append(b[m-1])
                b[m-1] = 0
                break
    return answer