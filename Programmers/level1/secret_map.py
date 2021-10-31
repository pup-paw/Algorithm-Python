def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        x = format(i | j, 'b').zfill(n)
        x = x.replace("1", "#")
        x = x.replace("0", " ")
        answer.append(x)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
