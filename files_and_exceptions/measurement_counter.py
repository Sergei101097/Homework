def measurement():
    p = 0
    oo = []
    myfile = open("numbers.txt", "r")
    m =myfile.readlines()
    for i in m:
        p+=1
        f = i.rstrip('\n')
        oo.append(f)
    l = len(oo)
    print(f"В файле 'numbers.txt' {l} строк")
measurement ()