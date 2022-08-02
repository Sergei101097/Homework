""" Задание №1 День недели."""

number = int(input('Введите число от 1 до 7: '))
if number == 1:
    print("Понидельник")
elif number == 2:
    print("Вторник")
elif number == 3:
    print('Среда')
elif number == 4:
    print('Четверг')
elif number == 5:
    print('Пятница')
elif number == 6:
    print('Cуббота')
elif number == 7:
    print('Воскресение')
else:
    print('Увы, цифра не верна.Попробуйте диапазон от 1 до 7')