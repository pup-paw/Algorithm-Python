#미완성
def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += str(4)
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n //= 3
    if n > 0:
        answer += str(n)
    return answer[::-1]


print(solution(30))
