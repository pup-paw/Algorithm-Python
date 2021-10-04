a, b, c = map(int, input().split())
if a + b + c >= 100:
    print("OK")
else:
    d = min(a, b, c)
    if d == a:
        print("Soongsil")
    elif d == b:
        print("Korea")
    else:
        print("Hanyang")
