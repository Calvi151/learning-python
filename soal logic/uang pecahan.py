uang = int(input("Masukkan jumlah uang (kelipatan 25): "))
pecahan = [1000, 500, 100, 50, 25]

for p in pecahan:
    jumlah = uang // p
    uang %= p
    print(f"{jumlah} pecahan Rp{p}")
