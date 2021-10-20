s = input()
n = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0
for i in range(len(s)):
    for x in n:
        if x.count(s[i]) == 1:
            t += n.index(x) + 3
print(t)
