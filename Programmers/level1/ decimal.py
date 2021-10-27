from itertools import combinations as cb


def solution(nums):
    answer = 0
    for a in cb(nums, 3):
        x = sum(a)
        for i in range(3, x):
            if x % i == 0:
                break
        else:
            answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
