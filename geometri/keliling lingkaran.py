print('-----------------------------------')
print('---menghitung keliling lingkaran---')
print('-----------------------------------')

pilihan=(input('masukan pilihan phi pertama atau kedua:\t'))

r=int(input('masukan nilai jari-jari:\t'))

if pilihan == 'pertama':
    phi=22/7
    
elif pilihan == 'kedua' :
    phi=3.14   
    
else:
    print('yang kamu masukan tidak valid')
    
hasil=2 * phi * r 
print(f"hasil lingkaran dengan jari-jari {r} cm adalah {hasil} cm.")

         