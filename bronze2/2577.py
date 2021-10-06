a = int(input())
a *= int(input())
a *= int(input())
l = list(str(a))
print(l)
for i in range(10):
    print(l.count(str(i)))
