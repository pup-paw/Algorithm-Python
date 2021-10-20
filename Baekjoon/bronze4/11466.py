l = sorted(map(int, input().split()))
a = l[1]/3 if l[1]/3 < l[0] else l[0]
b = l[0]/2
print(max(a, b))
