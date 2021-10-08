l = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# n = 0
# for i in range(len(c)):
for x in c:
    # if l.count(c[i]) != 0:
    #     n += l.count(c[i])
    l = l.replace(x, ',')
# l = l.replace(',', '')
# print(n + len(l))
print(len(l))
