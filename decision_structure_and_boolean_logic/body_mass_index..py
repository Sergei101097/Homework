massa = float(input('massa:'))

rost = float(input('rost:'))


imt = massa / rost

if 18.5 <= imt <= 25:
    print('imt norma')
elif imt < 18.5:
    print('IMT below normal')
else:
    print("more than normal")