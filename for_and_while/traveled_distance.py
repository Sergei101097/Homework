speed = int(input("Какая скорость транспортного средства в км/ч?: "))
time_1 = int(input("Сколько часов оно двигалось?: "))
print("Час\tПройденное растояние")
print("--------------------")
for im in range(1,time_1 + 1):
    total = speed * im
    print(im , "\t", total)

