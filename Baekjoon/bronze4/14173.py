a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

i = max(c, g) - min(a, e)
j = max(d, h) - min(b, f)

print(max(i, j)**2)
