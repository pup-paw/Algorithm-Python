c = int(input())
for i in range(c):
    l = list(map(int, input().split()))
    avg = sum(l)/l[0] - 1
    cnt = 0
    for i in range(1, l[0]+1):
        if l[i] > avg:
            cnt += 1
    print("{:.3f}%".format(cnt/l[0]*100))
