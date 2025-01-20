print('==PROGRAM PENGHITUNGAN NILAI MAHASISWA==')
nilai=int(input('masukan nilai siswa/siswi:\t'))
if nilai >= 80:
    print('Nilai A')
elif  70 <= nilai < 80:
    print('Nilai B')
elif  55 <= nilai < 70:
    print('Nilai C')
elif 40 <= nilai < 55:
    print('Nilai D')
elif nilai < 40:
    print('NIlai E')
else:
    print('Tryhard lagi nilai mu kecil')    