l = list(int(input()) for i in range(5))
t = 0

if l[0] < 0:
    t += abs(l[0]) * l[2]
    l[0] += abs(l[0])
if l[0] == 0:
    t += l[3]
if 0 <= l[0] < l[1]:
    t += (l[1] - l[0]) * l[4]

print(t)
