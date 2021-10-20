l = [input() for i in range(6)]
cnt = 0
for i in range(len(l)):
    if l[i] == "W":
        cnt += 1
if cnt < 1:
    print(-1)
elif cnt < 3:
    print(3)
elif cnt < 5:
    print(2)
else:
    print(1)
