a, b, c, d = map(int, input().split())
area = a/b * c/d / 2
if int(area) == area:
    print(1)
else:
    print(0)
