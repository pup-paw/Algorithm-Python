a = list(map(int, input().split()))
r = list(map(int, input().split()))
tmp = 0
for i in range(3):
    if r[i] - a[i] > 0:
        tmp += r[i] - a[i]
print(tmp)
