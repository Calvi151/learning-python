def habis_dibagi(number):
    if number % 2 == 0 and number % 3 == 0:
        return "Habis dibagi 2 dan 3"
    else:
        return "Tidak habis dibagi 2 dan 3"


print(habis_dibagi(12))   # Output: Habis dibagi 2 dan 3
print(habis_dibagi(10))  # Output: Tidak habis dibagi 2 dan 3
