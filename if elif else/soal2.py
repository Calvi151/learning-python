temperatur =float(input('masukan suhu dalam celcius:\t'))
if temperatur < 0:
    print("Sangat Dingin")
elif temperatur <= 15:
    print("Dingin")
elif temperatur <= 30:
    print("Hangat")
else:
    print("Panas")
