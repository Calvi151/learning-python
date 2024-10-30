print('====================')
print('PROGRAM LINGKARAN')
print("====================")
jari=int(input('masukan nilai jari-jari:\t'))
tinggi=int(input('masukan nilai tinggi:\t'))
phi=input('masukan nilai phi 22/7 atau 3.19:')
v= 0
if phi == '22/7':
    v= 2 * 22/7 * jari * tinggi 
elif phi == '3.19':
    v= 2 * 3.19 * jari * tinggi   
    print(f"tabung dengan jari-jari:\t{jari}\n dan tinggi:\t{tinggi}\n memiliki volume:{v} ")       