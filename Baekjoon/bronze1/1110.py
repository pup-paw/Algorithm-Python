n = int(input())
x = n
cnt = 0
while True:
    cnt += 1
    a = x % 10
    b = x // 10 + x % 10
    x = a * 10 + b % 10
    if x == n:
        break
print(cnt)
