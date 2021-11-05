def solution(record):
    answer = []
    uid = {}
    for r in record:
        if r.split()[0] != 'Leave':
            uid[r.split()[1]] = r.split()[2]
    for r in record:
        if r.split()[0] == 'Enter':
            answer.append(uid[r.split()[1]]+'님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            answer.append(uid[r.split()[1]]+'님이 나갔습니다.')
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
