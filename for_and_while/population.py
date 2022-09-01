
total = int(input('Введите стартовое кол-во организмов: '))
day_raising = int(input('Введите среднесуточное увеличение(в процентах): '))
days = int(input('Введите кол-во дней для размножения: '))
print('День\tПопуляция')
print('---------------')
for day in range(1, days+1):
    print(day, '\t', total)
    total+= total  * (day_raising / 100)

