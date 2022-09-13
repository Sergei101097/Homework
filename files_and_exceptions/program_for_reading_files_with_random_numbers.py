def total ():
    global oo
    oo = []
    outfile = open('philosophers.txt', 'r')
    m = outfile.readlines()
    amount_of_numbers(m)
def amount_of_numbers(h):

    for i in h:
        f = i.rstrip('\n')
        oo.append(f)
    l = len(oo)
    print(f"Кол-во случайных чисел в файле состовляет {l} шт")
    summa_list(l)
def summa_list(b):
    x = list(map(int,oo))
    v = sum(x)
    print(f"Сумма random чисел == {v}")

total()
