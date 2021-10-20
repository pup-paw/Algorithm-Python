a, b = map(int, input().split())
cnt = 1
while 1:
    if b*cnt - a*cnt >= b:
        break
    cnt += 1
print(cnt)
