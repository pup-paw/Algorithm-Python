import math

a, p1 = map(int, input().split())
r, p2 = map(int, input().split())

w = a / p1
s = (r * r * math.pi) / p2

if w > s:
    print("Slice of pizza")
else:
    print("Whole pizza")
