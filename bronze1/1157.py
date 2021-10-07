a = input().upper()
s = list(set(a))
l = list()
for x in s:
    l.append(a.count(x))
if l.count(max(l)) > 1:
    print("?")
else:
    print(s[l.index(max(l))])
