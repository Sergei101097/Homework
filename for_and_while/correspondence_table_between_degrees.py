degrees = int(input("Введите градусс по цельсию: "))
for nid in range(0,degrees + 1):
    f = (9/5)*nid+32
    print("Температура по Цельсии" ,nid,'\t',"Температура по Фаренгейту состовляет ",format(f,".1f"))

