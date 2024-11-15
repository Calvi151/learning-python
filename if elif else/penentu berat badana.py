bmi = 26  
bmi =float(input('masukan berat badan kamu:\t'))
if bmi < 18.5:
    print("Kurus")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Gemuk")
else:
    print("Obesitas")
