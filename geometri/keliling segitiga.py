print('****************************')
print('menghitung keliling segitiga')
print('****************************')

def segitiga():
    a=int(input('masukan nilai panjang sisi 1:\t'))
    b=int(input('msaukan nilai panjang sisi 2:\t'))
    c=int(input('masukan nilai panjang sisi 3:\t'))
    hasil= lambda a,b,c: a + b + c
    print('hasil penjumlahannya adalah:\t',hasil)
segitiga()