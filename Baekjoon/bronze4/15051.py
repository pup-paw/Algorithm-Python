l = list(int(input()) for i in range(3))
print(min(l[1]*2+l[2]*4, l[0]*2+l[2]*2, l[0]*4+l[1]*2))
