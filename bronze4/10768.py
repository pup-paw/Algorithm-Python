y = int(input())
m = int(input())

if y < 2 or (y == 2 and m < 18):
    print("Before")
elif y == 2 and m == 18:
    print("Special")
else:
    print("After")
