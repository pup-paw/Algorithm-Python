def solution(s):
    answer = [len(s)]
    x = 1
    for i in range(1, (len(s))//2+1):
        answer.append('')
        for j in range(0, len(s), i):
            if j + i <= len(s)-1 and s[j:i+j] == s[i+j:2*i+j]:
                x += 1
            elif x == 1:
                answer[i] += s[j:i+j]
            else:
                answer[i] += str(x)+s[j:i+j]
                x = 1
        answer[i] = len(answer[i])
    return min(answer)


print(solution("a"))
