import math
a, b, c = map(int, input().split())
d = 0
for i in range(math.ceil(c/a)):
    if c <= 0:
        break
    c -= a
    d += 1
    if d % 7 == 0:
        c -= b
print(d)
