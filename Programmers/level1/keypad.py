def solution(numbers, hand):
    num1 = [1, 4, 7]
    num2 = [2, 5, 8, 0]
    num3 = [3, 6, 9]
    r = [3, 2]
    l = [3, 0]
    answer = ''

    for n in numbers:
        if n in num1:
            answer += 'L'
            l = [num1.index(n), 0]
        elif n in num3:
            answer += 'R'
            r = [num3.index(n), 2]
        else:
            now = [num2.index(n), 1]
            dr = abs(r[0]-now[0]) + abs(r[1]-now[1])
            dl = abs(l[0]-now[0]) + abs(l[1]-now[1])
            if dr > dl or (dr == dl and hand == "left"):
                answer += 'L'
                l = now
            else:
                answer += 'R'
                r = now

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
