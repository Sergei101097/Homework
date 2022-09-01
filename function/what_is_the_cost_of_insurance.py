def prace_house():
    prace = float(input("Введите цену за дом в ($): "))
    insurance(prace)
def insurance(prace):
    totol_insurance = prace * 0.8
    print(f"Сумма страховски составит {totol_insurance} $")
prace_house()