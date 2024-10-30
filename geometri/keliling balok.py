print('=========================')
print('==menghitung luas balok==')
print('=========================')
def balok ():
    panjang=int(input('masukan nilai panjang:\t'))
    lebar=int(input('masukan nilai sisi:\t'))
    tinggi=int(input('masukan nilai tinggi:\t'))

    hasil= lambda panjang,lebar,tinggi:panjang * lebar * tinggi
    print('hasil penjumlahan:\t',hasil) 
balok()