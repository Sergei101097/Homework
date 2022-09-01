def total_car():
    prace_car = float(input("Введите затраты на топливо за 1 мес: "))
    prace_car_1 = float(input("Введите затраты на кредит за 1 мес: "))
    prace_car_2 = float(input("Введите затраты на СТО за 1 мес: "))
    prace_month(prace_car,prace_car_1,prace_car_2)
    prace_year(prace_car, prace_car_1, prace_car_2)

def prace_month(x,y,z):
    total_mont = x + y + z
    print(f"Ваши растраты за 1 мес составят {total_mont} руб")

def prace_year(x,y,z):
    total_mont = ( x + y + z ) * 12
    print(f"Ваши рассходы за 1 год составят {total_mont} руб")
total_car()