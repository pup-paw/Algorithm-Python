def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    chr = "~!@#$%^&*()=+[{]}:?,<>/"
    new_id = ''.join(x for x in new_id if x not in chr)
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    # 5
    if len(new_id) == 0:
        new_id = "a"
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    # 7
    if len(new_id) <= 2:
        for i in range(3-len(new_id)):
            new_id += new_id[-1:]

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
