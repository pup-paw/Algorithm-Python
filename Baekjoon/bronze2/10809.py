l = list(input())
for x in range(97, 123):
    if l.count(chr(x)) == 0:
        print(-1, end=' ')
    else:
        print(l.index(chr(x)), end=' ')
