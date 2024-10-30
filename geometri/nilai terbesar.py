nilai_r=int(input('Masukan  Nilai R:\t'))
nilai_s=int(input('Masukan Nilai S:\t'))
nilai_x=int(input('Masukan Nilai X:\t'))
       
if nilai_r > nilai_s:
    print('Nilai R lebih besar')
elif nilai_s > nilai_r:
    print('Nilai S sedang')
elif nilai_x < nilai_s < nilai_r:
    print('Nilai X Terkecil')   
print(f'nilai terbesar adalah:{nilai_r}\t\tNilai Sedang Adalah S:{nilai_s}\t\tNilai terkecil adalah X:{nilai_x}')