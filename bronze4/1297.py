import math
d, h, w = map(int, input().split())
print(int(h*d/math.sqrt(h*h+w*w)), int(w*d/math.sqrt(h*h+w*w)))
