def tax():
    tax_1 = float(input("Введите цену дома: "))
    assessed_value(tax_1)
def assessed_value(val):
    total_assessed = val * 0.6
    assessed_value_tax(total_assessed)
    print(total_assessed)
def assessed_value_tax(val):
    total_assessed_value_tax = (val / 100)* 0.72
    print(format(total_assessed_value_tax,".2f"))

tax()

