pak = int(input('Введите кол-во приобретаемой ПО: '))

if 10 <= pak <= 19:
    discount = (pak * 99) * 0.10
    pak_1 = (pak * 99) - discount
    print("Скидка составит", format(discount, '.2f'), f"Итого(со скидкой): {pak_1}")
elif 20 <= pak <= 49:
    discount = (pak * 99) * 0.20
    pak_1 = (pak * 99) - discount
    print("Скидка составит", format(discount, '.2f'), f"Итого(со скидкой): {pak_1}")
elif 50 <= pak <= 99:
    discount = (pak * 99) * 0.30
    pak_1 = (pak * 99) - discount
    print("Скидка составит", format(discount, '.2f'), f"Итого(со скидкой): {pak_1}")
elif 100 <= pak:
    discount = (pak * 99) * 0.40
    pak_1 = (pak * 99) - discount
    print("Скидка составит", format(discount, '.2f'), f"Итого(со скидкой): {pak_1}")
else:
    print('Прошу прощение, сейчас подойдет менеджер')