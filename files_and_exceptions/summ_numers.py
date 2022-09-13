def summa_numbers():
    p = 0
    oo = []
    myfile = open("numbers.txt", "r")
    m =myfile.readlines()
    for i in m:
        p+=1
        f = i.rstrip('\n')
        oo.append(f)
    x=list(map(int, oo))
    v =sum(x)
    print(f"Сумма числовых значений из файла 'frr.txt' составила {v}")

summa_numbers()