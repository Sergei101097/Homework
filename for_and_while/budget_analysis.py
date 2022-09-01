stop = 'Da'
while stop == 'Da':
    wod = int(input("Введите свою зп за мес: "))
    wod_1 =int(input("Введите цену аз кв: "))
    wod_2 = int(input("Введите цену за еду: "))
    total = wod_2 + wod_1
    j = wod - total
    if wod > total:
        print(f"У вас осталось на прочие расходы {j}р")
    else:
        print(f"Увы ва ушли в {j}р")
    stop = str(input("Если желаете продолжить введите 'Da': "))