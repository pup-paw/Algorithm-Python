a = int(input())
cnt = 0
for i in range(1, a+1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        l = list(str(i))
        if int(l[0]) + int(l[2]) == 2 * int(l[1]):
            cnt += 1
print(cnt)
