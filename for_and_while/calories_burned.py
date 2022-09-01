CALORIES = 4.2
stop = 'Da'
while stop == 'Da':
    time_cal = int(input("Введите кол-во (мин) бега:  "))
    total_sport_calories = time_cal * CALORIES
    print("Во время бега вы потеряли",format(total_sport_calories, ".2f"),"калл")
    stop = str(input("Если желаете продолжить введите 'Da': "))