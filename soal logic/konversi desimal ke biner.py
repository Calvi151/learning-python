desimal = int(input("Masukkan bilangan desimal: "))
biner = bin(desimal)[2:]  # Menghilangkan '0b' di depan
print("Bilangan biner:", biner)