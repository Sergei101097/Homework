gody = int(input('Укажите количество лет: '))
osadki_vsego = 0
for god in range(1, gody +1):
    for mes in['Январе', 'Феврале', 'Марте', 'Апреле', 'Мае', 'Июне', 'Июле', 'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре']:
        zapros = 'Укажите количество осадков в ' + mes + '\t' + str(god) + '-го года: '
        osadki = int(input(zapros))
        osadki_vsego = osadki_vsego + osadki
mes_vsego = gody * 12
osadki_sred = osadki_vsego / mes_vsego
print('Всего месяцев:', mes_vsego)
print('Всего осадков:', osadki_vsego, 'мм')
print('Среднее количество осадков:', format(osadki_sred, '.2f'), 'мм')