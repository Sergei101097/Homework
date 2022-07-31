"""Задание №2 Проrноз продаж."""
total_income = int(input("Ввести плановую сумму общего объема продаж:"))

INTEREST_RATE = 0.23


profit = total_income * INTEREST_RATE

profit = format(profit, '.2f')

print(profit)