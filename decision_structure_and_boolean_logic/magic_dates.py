data = int(input('Введите дату: '))
montag = int(input('Введите месяц (цифра): '))
yar = int(input('Введите год (последнии 2 цифры): '))

data_montag = data * montag

if data_montag == yar:
    print('Данная дата волшебная')
else:
    print("Данная дата не являеться волшебной")