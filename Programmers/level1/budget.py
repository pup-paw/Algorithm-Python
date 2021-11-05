def solution(d, budget):
    answer = 0
    for x in sorted(d):
        budget -= x
        if budget < 0:
            break
        answer += 1
    return answer


print(solution([2, 2, 3, 3], 10))
