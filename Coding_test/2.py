def solution(log):
    answer = 0
    for i in range(0, len(log)-1, 2):
        start_h, start_m = map(int, log[i].split(":"))
        stop_h, stop_m = map(int, log[i+1].split(":"))
        t = (stop_h - start_h) * 60 + (stop_m - start_m)
        if t >= 105:
            answer += 105
        elif t >= 5:
            answer += t
    return str(answer//60).zfill(2)+":"+str(answer % 60).zfill(2)


print(solution(["08:30", "09:00", "14:00", "16:00",
               "16:01", "16:06", "16:07", "16:11"]))
