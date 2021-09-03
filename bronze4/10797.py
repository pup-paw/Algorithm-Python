a = int(input())
l = list(map(int, input().split()))
count = 0

for i in range(len(l)):
    if l[i] == a:
        count += 1

print(count)
