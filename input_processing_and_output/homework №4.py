"""Задание №4 Общий объем продаж."""

prace_1 = float(input("Введите цену товара №1:"))
prace_2 = float(input("Введите цену товара №2:"))
prace_3= float(input("Введите цену товара №3:"))
prace_4 = float(input("Введите цену товара №4:"))
prace_5 = float(input("Введите цену товара №5:"))

SALES_TAX = 0.07

sum_prace = prace_1 + prace_2 + prace_3 + prace_4 + prace_5

total = (prace_1 + prace_2 + prace_3 + prace_4 + prace_5 ) * SALES_TAX
print( f"Итог за 5 покупок:{sum_prace} бел.р","Сумма с налога:",format(total, '.2f'),"бел.р")
