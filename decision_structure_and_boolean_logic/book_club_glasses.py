book = int(input("Введите кол-во книг: "))

if book <= 6:
    t = book * 5
    print(f'Вы получили {t} очков')
elif 7 <= book:
    t = (book * 60) / book
    print(f"Вы получаете {t} очков")
else:
    print('Ошибка ввода ')