x=0
for a in range(2, 11, 2):
    if a < 10:
        print(a, end=' + ')
    else:
        print(a, end=' = ')
    x = x + (a)
print(x)