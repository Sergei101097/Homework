salary = int(input("З/п: "))
working_day = int(input("Введите кол-во отработаных дней: "))
for i in range(working_day+1):
    salary = salary * 2
    total_rub = salary / 100
    print(f"Ваша З/П составила{total_rub}рубля")
