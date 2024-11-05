# Ukuran belah ketupat
n = 5

# Bagian atas belah ketupat
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

# Bagian bawah belah ketupat
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)
# Ukuran setengah belah ketupat