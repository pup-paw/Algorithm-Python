ah1, am1, as1, ah2, am2, as2 = map(int, input().split())
bh1, bm1, bs1, bh2, bm2, bs2 = map(int, input().split())
ch1, cm1, cs1, ch2, cm2, cs2 = map(int, input().split())


def f(a, b, c, d, e, f):
    if f-c < 0:
        if e-b <= 0:
            print(d-a-1, e-b+60-1, f-c+60)
        else:
            print(d-a, e-b-1, f-c+60)
    else:
        print(d-a, e-b, f-c)


f(ah1, am1, as1, ah2, am2, as2)
f(bh1, bm1, bs1, bh2, bm2, bs2)
f(ch1, cm1, cs1, ch2, cm2, cs2)
