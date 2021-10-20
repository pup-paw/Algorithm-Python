x = int(input())
i = 1
j = 2
while i < x:
    i += j
    j += 1
a = i - x + 1
b = j - a
if j % 2 == 0:
    print(str(a)+'/'+str(b))
else:
    print(str(b)+'/'+str(a))
