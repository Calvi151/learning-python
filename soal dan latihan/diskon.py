print('='*20)
print('ONE PRIDE CHICKEN')
print('='*20)

menu={
    "Chicken":12000,
    "Burger":15000,
    "Kebab":10000,
}
print(menu)

m=int(input('masukan total belanja:\t'))

if m > 50000:
    total = m - 5000
    print(total)
    
