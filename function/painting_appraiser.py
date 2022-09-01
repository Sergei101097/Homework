prais_farba_work = []
def work ():
    kw = float(input("Введите м2 который надо покрасить: "))
    prais_farba = float(input("Введите цену за красску: "))
    farba_work(kw)
    total_mani_work(prais_farba_work,kw,prais_farba)
def farba_work(far):

    total_farba = far / 10
    litr_farba = total_farba * 5
    time_work = total_farba * 8
    prais_farba_work.append(time_work)
    print(f"Для покраски {far} m2 , потребуется {total_farba} банка(и)  или {litr_farba} литр(ов) краски")
    print(f"Для выполнения работы потреюуеться {time_work} часов ")
def total_mani_work(tmw,m_2,pf):
    prais_work = tmw * 2000
    m = (m_2 / 10) * pf
    pw = sum(prais_work)
    j = pw + m
    print(f"Цена за покраску {m_2} m2, составит {pw} р" )
    print(f"Краска обойдеться вам в {m} р ")
    print(f"ИТОГ стоимость составила: {j} р")

work()