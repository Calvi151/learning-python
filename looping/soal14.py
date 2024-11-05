# Ukuran setengah belah ketupat
n = 5

# Bagian atas setengah belah ketupat
for i in range(1, n+1):
    if i == n:
        print(" " * (n-i) + "* " * (i + 2))  # Bagian tengah dengan 3 bintang tambahan
    else:
        print("* " * i)

# Bagian bawah setengah belah ketupat
for i in range(n-1, 0, -1):
    if i == n / 2:
        print("* " * (i + 2))  # Bagian tengah dengan 3 bintang tambahan
    else:
        print("* " * i)
