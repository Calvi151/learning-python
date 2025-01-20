n = int(input("Masukkan nilai N: "))
print("Bilangan genap dari 1 hingga", n, ":")
for i in range(2, n + 1, 2):
    print(i, end=' ')