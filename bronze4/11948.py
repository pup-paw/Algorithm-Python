l = list(int(input()) for i in range(6))
print(sum(l)-min(l[0], l[1], l[2], l[3])-min(l[4], l[5]))
