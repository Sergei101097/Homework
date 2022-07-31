"""Задание №3 Расчет площади земельного участка."""


SQUARE_METER = 4046.8564224
acre_of_land = float(input("Введите кол-во АКР:"))
total = acre_of_land * SQUARE_METER

print(f"{acre_of_land} АКР состовляет", format(total, '.2f') ,"кв.м")