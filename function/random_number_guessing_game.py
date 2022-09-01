import random
def random_numer_game():
    f = 0
    po = int(input("Введите кол-во попыток: "))
    while f < po:
        f+=1
        print("Приветствую в игре угадай число")
        i = int(input("Введите число от 1 до 100: "))
        j = random.randint(0, 100)
        kul(i,j)
def kul(val,ki):
        if val > ki:
            print(f"Увы противник загадал число {ki}")
        elif val < ki:
            print(f"Увы противник загадал число {ki}")
        else:
            print(f"Ваш противник загадал такоеже число{ki}")
random_numer_game()



