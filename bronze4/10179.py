a = int(input())
l = [float(input()) for i in range(a)]
for i in range(a):
    print("${:.2f}".format(l[i]*0.8))
