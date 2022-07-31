"""Задание №6 Расход бензина в расчете на километры пройденного пути."""

kilometers_traveled = int( input("Введите пройденый путь(км):"))

fuel_consumption = float(input("Введите рассход топлива вашего ТС:"))

total = (fuel_consumption / kilometers_traveled) * 100
print(f"Расход вашего ТС  составил ", format(total, '.2f'), f'л на 100 км')
