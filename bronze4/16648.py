t, p = map(int, input().split())
x = 0
if p <= 20:
    x = t / (120 - 2 * p)
    print(p * 2 * x)
else:
    x = t / (100 - p)
    print((p - 20) * x + 20 * 2 * x)
