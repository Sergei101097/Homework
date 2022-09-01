def future_val():
    mani = float(input("Текущая стоимость: "))
    sail = float(input("Процентная ставка (r): "))
    year = int(input("Количество периодов (мес) (n): "))
    total(mani,sail,year)
def total(m,s,y):
    for h in range(1,y+1):
        sal = s / 100
        F = m * (sal + 1)**h
        print(f"В {h} мес, ваш счет будет состовлять: ",format(F,".2f")," р")
future_val()