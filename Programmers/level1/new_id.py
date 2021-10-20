def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    chr = "~!@#$%^&*()=+[{]}:?,<>/"
    new_id = ''.join(x for x in new_id if x not in chr)
    # 3
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and new_id[i-1] == '.':
            new_id.replace(new_id[i], '')
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
