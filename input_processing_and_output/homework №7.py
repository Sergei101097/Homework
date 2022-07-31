"""Задание № 7 Чаевые, налоr и общая сумма."""
sum_check = int(input("Введите сумму своего чека:"))

NALOG = 0.07
NACHAI = 0.18

total = sum_check * NALOG
total_1 = sum_check * NACHAI
total_3 = sum_check + total_1 +total
print(f"Сумма чека:{sum_check} бел.р","\nСумма налога составила:", format(total, '.2f'),"бел.р",f"\nСумма чаевых составила:{total_1} бел.р \nИтоговая (Сумма чека + налог + чай): {total_3} бел.р")
