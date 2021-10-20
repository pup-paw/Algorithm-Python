t = int(input())
a, b, c = 0, 0, 0
if t % 10 != 0:
    print(-1)
else:
    a = t//300
    t -= a*300
    b = t//60
    t -= b*60
    c = t//10
    print(a, b, c)
