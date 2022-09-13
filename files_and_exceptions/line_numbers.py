def lin_number():
    p = 0
    myfile = open("numbers.txt", "r")
    m_r =myfile.readlines()
    for i in m_r:
        p+=1
        print(f"Cтрокa №{p}: Значение {i}")
lin_number()