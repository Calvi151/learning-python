d=0
for c in range(1, 6):
    if d < 5:
        print(c, end=' + ')
    else:
        print(c, end=' = ')
    d= d + (c)
print(d)