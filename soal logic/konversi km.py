cm = int(input("Masukkan jarak dalam cm: "))
km = cm // 100000
m = (cm % 100000) // 100
cm = cm % 100
print(f"{km} km, {m} m, {cm} cm")
