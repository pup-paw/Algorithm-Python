a = int(input())
a *= int(input())
a *= int(input())
l = list(str(a))
for i in range(10):
    print(l.count(str(i)))
