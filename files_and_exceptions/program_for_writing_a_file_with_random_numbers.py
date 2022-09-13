import random
def random_number_enter_users ():

    i = int(input("Введите кол-во случайный чисел: "))
    outfile = open('philosophers.txt', 'w')
    for o in range(i):
        pas = random.randint(1,500)
        outfile.write(str(pas) + '\n')
    print(f"{i} random чисел были сохранены в фале 'philosophers.txt'")

random_number_enter_users()
