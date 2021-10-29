def solution(arr):
    answer = []
    for i, x in enumerate(arr):
        if i == 0 or x != answer[-1]:
            answer.append(x)
    return answer


print(solution([4, 4, 4, 3, 3]))
