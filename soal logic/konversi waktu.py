detik = int(input("Masukkan jumlah detik: "))
hari = detik // (24 * 3600)
sisa = detik % (24 * 3600)
jam = sisa // 3600
sisa %= 3600
menit = sisa // 60
detik = sisa % 60
print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")
