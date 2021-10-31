def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for x in s:
        print(x)
        print(ord(x))
        if not (47 < ord(x) < 58):
            return False
    return True


print(solution("1234"))
