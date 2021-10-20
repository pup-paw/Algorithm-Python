l = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for x in c:
    l = l.replace(x, ',')
print(len(l))
