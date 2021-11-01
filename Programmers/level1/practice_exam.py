def solution(answers):
    answer = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, x in enumerate(answers):
        if x == a[i % len(a)]:
            answer[0] += 1
        if x == b[i % len(b)]:
            answer[1] += 1
        if x == c[i % len(c)]:
            answer[2] += 1
    return [i+1 for i, val in enumerate(answer) if val == max(answer)]


print(solution([1, 2, 3, 4, 5]))
