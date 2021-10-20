s = set(i for i in range(1, 10001))
a = set()
for i in range(1, 10001):
    d = 0
    d += i
    for j in str(i):
        d += int(j)
    a.add(d)
b = s - a
for x in sorted(b):
    print(x)
