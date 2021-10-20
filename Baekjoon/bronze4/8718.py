x, k = map(int, input().split())
if k + k*2 + k*2*2 <= x:
    print(int((k+k*2+k*2*2)*1000))
elif k/2 + k + k*2 <= x:
    print(int((k/2+k+k*2)*1000))
elif k/2/2 + k/2 + k <= x:
    print(int((k/2/2+k/2+k)*1000))
else:
    print(0)
