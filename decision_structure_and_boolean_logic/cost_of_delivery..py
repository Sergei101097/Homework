i = int(input('Введите массу: '))

if i <= 200:
    prace =  (i / 100)  * 150
    print("Цена за груз составит", format(prace, '.2f'))

elif 200 <= i <= 600:
    prace = (i / 100) * 300
    print("Цена за груз составит", format(prace, '.2f'))
elif 600 <= i < 1000:
    prace = (i / 100) * 400
    print("Цена за груз составит", format(prace, '.2f'))

elif  1000 <= i:
    prace =  (i / 100)  * 475
    print("Цена за груз составит", format(prace, '.2f'))
else:
    print('Ошибка')
