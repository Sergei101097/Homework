book = int(input("Введите кол-во книг: "))

if book <= 6:
    y = book * 5
    print(f'Вы получили {y} очков')
elif 7 <= book:
    y = (book * 60) / book
    print(f"Вы получаете {y} очков")
else:
    print('Ошибка ввода ')