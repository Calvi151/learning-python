angka=int(input('masukan angka pertama:\t'))
angka2=int(input('masukan angka ke 2:\t'))
angka3=int(input('masukan angka ke 3:\t'))

if angka >= angka2 and angka >= angka3:
    print(f'angka tebesar adalah{angka}')
elif angka2 >= angka and angka2 >= angka3:
    print(f'angka terbesar adalah{angka2}')
else:
    print(f'angka terbesar adalah{angka3}')