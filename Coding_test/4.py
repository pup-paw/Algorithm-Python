def solution(s):
    answer = []
    i = 0
    while True:
        if i == len(s)-1 or s[i] != s[i+1]:
            break
        i += 1
    s += s[:i+1]
    s = s[i+1:]
    tmp = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            tmp += 1
        else:
            answer.append(tmp)
            tmp = 1
    answer.append(tmp)

    return sorted(answer)


print(solution("wowwow"))
