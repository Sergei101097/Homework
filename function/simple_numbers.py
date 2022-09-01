def simple_num():
    h = int(input("Введи число и узнай, простое оно ил нет: "))
    g(h)
def g (val):
    f = range(1,100)
    k = []

    for i in f:
        if val % i == 0:
            k.append(i)
    if k[0] == 1 and k[1] == val:
            print('Простое число ')
    else:
            print("Непрсотое число")
simple_num()







