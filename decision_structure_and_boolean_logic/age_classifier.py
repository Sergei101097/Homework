age = int(input('Введите свой возраст: '))

if age <= 1:
    print('Вы младенец')
elif 2 == age or age <= 13:
    print('Вы ребенок')
elif age == 14 or age <= 20:
    print('Вы подросток')
else:
    print('Вы взрослый')