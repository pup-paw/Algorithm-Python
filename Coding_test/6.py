def solution(time, plans):
    answer = ''
    monday = 13
    friday = 18
    for p in plans:
        m = int(p[2][:len(p[2])//2])
        if p[2][-2:] == "PM":
            m += 12
        if m > monday:
            time -= m - monday
        f = int(p[1][:len(p[1])//2])
        if p[1][-2:] == "PM":
            f += 12
        if f < friday:
            time -= friday - f
        if time <= 0:
            break
        answer = p[0]
    return answer


print(solution(3.5, [["홍콩", "11PM", "9AM"], [
      "엘에이", "3PM", "11AM"], ["오사카", "8PM", "1PM"]]))
