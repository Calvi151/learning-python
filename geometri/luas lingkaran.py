print('-----------------------------------')
print('-----menghitung luas lingkaran-----')
print('-----------------------------------')

pilihan=(input('masukan pilihan phi jago atau senior:\t'))

r=int(input('masukan nilai jari-jari:\t'))

if pilihan == 'jago':
    phi=22/7
    
elif pilihan == 'senior' :
    phi=3.14   
    
else:
    print('yang kamu masukan tidak valid')
    
hasil= phi * r 
print(f"hasil lingkaran dengan jari-jari {r} cm adalah {hasil} cm.")

         