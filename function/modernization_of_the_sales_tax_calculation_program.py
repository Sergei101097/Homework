def summa():
    total_sum = int(input("Введите сумму за товар: "))
    print(f"С суммы {total_sum} руб")
    federal_tax(total_sum)
    regional_tax(total_sum)
def federal_tax(val):
    j = val * 0.05
    print(f"Региональный налог составит {j} руб")
def regional_tax(val):
    j = val*0.23
    print(f"Фидиральный налог составит {j} руб")

summa()