import random
def rock_pager_scissors():
    f = 0
    po = int(input("Введите кол-во попыток: "))
    while f < po:
        f+=1
        i = str(input("введите: "))
        list = ["камень", "ножницы", "бумага"]
        computer_action = random.choice(list)
        kul(i,computer_action,f)
def kul(val,ca,a):
        if val == ca:
            print(f"Оба пользователя выбрали {val}. Ничья!!")
            print(f"вы угадали с {a} попытки")
        elif val == "камень":
            if ca == "ножницы":
                print(f"Камень бьет ножницы! Вы победили! c {a}  попытки")
            else:
                print(f"Бумага оборачивает камень! Вы проиграли. это была {a} попытка")
        elif val == "бумага":
            if ca == "камень":
                print("Бумага оборачивает камень! Вы победили!")
            else:
                print(f"Ножницы режут бумагу! Вы проиграли.это была {a} попытка")
        elif val == "ножницы":
            if ca == "бумага":
                print("Ножницы режут бумагу! Вы победили!")
            else:
                print(f"Камень бьет ножницы! Вы проиграли.это была {a} попытка")
rock_pager_scissors()