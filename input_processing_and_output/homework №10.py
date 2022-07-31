"""Задание №10 Процент учащихся обоего пола."""
boy = int(input("Введите кол-во мальчиков:"))
girl = int(input("Введите кол-во девочек:"))

total = boy + girl

boy_procent = (boy / total) * 100
girl_procent = (girl / total) * 100

print(f"Мальчиков состовляет {boy_procent} %\nДевочек состовляет {girl_procent} %")
