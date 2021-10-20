a, b = map(int, input().split())
if a == 0:
    q = 0
    r = 0
elif a < 0:
    q = abs(a) // abs(b) + 1
else:
    q = abs(a) // abs(b)
if a * b < 0:
    q = -q
r = a - b * q

print(q)
print(r)
