def solution(x, n):
    return list(x*(i+1) for i in range(n))


print(solution(2, 5))
