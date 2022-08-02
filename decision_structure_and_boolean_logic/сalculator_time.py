i = int(input())

if  i <= 3600:
    g = i // 60
    print(format(g, '.2f'), " минут")

elif 3600 <= i <= 86800:
    g = i // 3600
    print(format(g, '.2f'), 'часов')

elif 86400 <= i:
    g = i //86400

    print(f"{g} дней")