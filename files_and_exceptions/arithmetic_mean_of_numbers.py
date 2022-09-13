def arithmetic():
    p = 0
    oo = []
    myfile = open("numbers.txt", "r")
    m =myfile.readlines()
    for i in m:
        p+=1
        f = i.rstrip('\n')
        oo.append(f)
    l = len(oo)
    x=list(map(int, oo))
    v =sum(x)
    total_sred = v / l
    print(f"Среднее арефмитическое составило {total_sred}")
arithmetic()