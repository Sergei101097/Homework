UGLI = 4
SHIR = 9
total_kallo = []
def calories():
    carbohydrates = float(input("Введите углеводы в граммах: "))
    fats = float(input("Введите жиры в граммах: "))
    carbohydrates_1(carbohydrates)
    fats_1(fats)
    sum_carbohydrates_fats (total_kallo)
def carbohydrates_1(car):
    carbohydrates = car * UGLI
    total_kallo.append(carbohydrates)
    print(f"{car} грамм углеводов  это , {carbohydrates} каллорий")
def fats_1(fat):
    fats = fat * SHIR
    total_kallo.append(fats)
    print(f"{fat} грамм жира это , {fats} каллорий")
def sum_carbohydrates_fats(total):
    t_kal = sum(total)
    print(f"Общее кол-во каллорий составило {t_kal}")

calories()