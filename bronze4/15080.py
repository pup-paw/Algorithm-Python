a = list(map(int, input().split(" : ")))
b = list(map(int, input().split(" : ")))
tmp = (b[0]-a[0])*3600+(b[1]-a[1])*60+(b[2]-a[2])
if tmp < 0:
    b[0] += 24

print((b[0]-a[0])*3600+(b[1]-a[1])*60+(b[2]-a[2]))
