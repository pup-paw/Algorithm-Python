def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    return sorted(answer) if len(answer) > 0 else [-1]


print(solution([3, 2, 6], 10))
