# massa = float(input("Введите массу своего тела: "))
# tim = int(input("Введите время сушки(в мес): "))
# MONTH= 0
# while MONTH +1 < tim:
#     fats = 1.5 * MONTH
#     total = massa - fats
#     MONTH+=1
#     print(f"Ваш вес на {MONTH} месяц,составит {total} kg")
#



massa = float(input("Введите массу своего тела: "))
tim = int(input("Введите время сушки(в днях): "))
print("День\tКаллории\tЖиры")
print("-----------------------")
for i in range(tim+1):

    fats = 500 * i
    total_mass_in_kg = fats/9000
    total = massa - fats
    print(i,'\t',fats,'\t',format(total_mass_in_kg,".2f"))
