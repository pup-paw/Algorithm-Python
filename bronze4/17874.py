n, h, v = map(int, input().split())
s = max(h, n - h) * max(v, n - v)
print(s * 4)
