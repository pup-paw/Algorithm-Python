n = int(input())
for i in range(n):
    l = ['X']
    l += list(input())
    r = [0]
    for j in range(1, len(l)):
        if l[j] == 'O':
            r.append(r[j-1] + 1)
        else:
            r.append(0)
    print(sum(r))
