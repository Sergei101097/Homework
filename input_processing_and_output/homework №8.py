""" Заданеи № 8 Преобразователь температуры по шкале Цельсия в температуру по шкале Фаренгейта"""

celsius = float(input("Введите температуру по цельсию: "))

fahrenheit = 9 / 5 * celsius + 32
print(format(fahrenheit, '.2f'))