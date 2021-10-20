l = [0]*5
for i in range(len(l)):
    l[i] = int(input())
    if l[i] < 40:
        l[i] = 40
print(sum(l)//5)
