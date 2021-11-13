def solution(arr):
    t = max(arr.count(1), arr.count(2), arr.count(3))
    return list(t - arr.count(i) for i in range(1, 4))
    return [t-arr.count(1), t-arr.count(2), t-arr.count(3)]


print((solution([2, 1, 3, 1, 2, 1])))
