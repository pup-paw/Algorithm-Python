a = int(input())
if a // 10 <= 10:
    print((a // 10) + (a % 10))
else:
    print((a // 100) + (a % 100))
