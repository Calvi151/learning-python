nama_bulan=['januari','Februari','Maret','April','Mei','Juni','July','Agustus','September','Oktober','November','Desember']

print(nama_bulan[2])
print(nama_bulan[9])
nama_bulan[0] = 'January'
nama_bulan[7] = 'August'
nama_bulan.append('Muharam')
for r,o in enumerate(nama_bulan):
    print(f"bulan ke-{r+1} yaitu {o}")