def solution(N, stages):
    failure = {i: 0 for i in range(1, N+1)}
    stage = len(stages)
    for i in failure.keys():
        stage -= stages.count(i-1)
        if stage == 0:
            break
        failure[i] = stages.count(i) / stage
    # return list(
    #     dict(sorted(failure.items(), key=lambda x: x[1], reverse=True)).keys())
    return sorted(failure, key=lambda x: failure[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
