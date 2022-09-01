sum_bal_total = []
def bal():
    i_1 = float(input("Ведите полученый бал за 1 экзамен: "))
    i_2 = float(input("Ведите полученый бал за 2 экзамен: "))
    i_3 = float(input("Ведите полученый бал за 3 экзамен: "))
    i_4 = float(input("Ведите полученый бал за 4 экзамен: "))
    i_5 = float(input("Ведите полученый бал за 5 экзамен: "))
    sum_bal_total.append(i_5)
    sum_bal_total.append(i_4)
    sum_bal_total.append(i_3)
    sum_bal_total.append(i_2)
    sum_bal_total.append(i_1)
    sum_bal(sum_bal_total)
def sum_bal(bal):
    total_bal = sum(bal)
    if total_bal < 60:

            print("Ваш уровень знаний 'F'")

    elif 60 < total_bal <= 69:

            print("Ваш уровень знаний 'D'")

    elif 70 < total_bal <= 79:

            print("Ваш уровень знаний 'C'")

    elif 80 < total_bal <= 89:

            print("Ваш уровень знаний 'B'")

    else:
            print("Ваш уровень знаний 'A'")
    average_mark = total_bal / 5
    print(f"Общая сумма ваших балов составило {total_bal}")
    print(f"Средний бал составил {average_mark}")
bal()