def solution(N, stages):
    faillure = {i: 0 for i in range(1, N+1)}
    for stage in stages:
        if stage > 1:
            faillure[stage-1] += 1
    return sorted(faillure.items(), key=lambda x: x[1])


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
