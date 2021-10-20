def solution(lottos, win_nums):
    tmp = len(set(lottos) & set(win_nums))  # 교집합 (instersection으로도 사용 가능)
    zero = lottos.count(0)
    answer = [7-max(tmp+zero, 1), 7-max(tmp, 1)]
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
