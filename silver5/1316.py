n = int(input())
r = 0
for i in range(n):
    c = input()
    j = 0
    l = list()
    for x in c:
        if j > 0 and l.count(x) > 0 and l[j-1] != x:
            break
        l.append(x)
        j += 1
    if j == len(c):
        r += 1
print(r)
