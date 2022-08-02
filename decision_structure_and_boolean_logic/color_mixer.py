coller = str(input('Выберите цвет (красный, синий, желтый): '))
coller_2 = str(input('Выберите цвет (красный, синий, желтый): '))

if coller ==  "красный"  and coller_2 == "синий" :
    print('фиолетоввый')
elif coller == "красный" and  coller_2 == "желтный":
    print('оранжевый')
elif coller == "синий"  and  coller_2 == "желтый":
    print('зеленый')
else:
    print("Прошу прощение, я не знаю какой будет цвет )")