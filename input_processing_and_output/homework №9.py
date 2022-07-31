""" Задание № 9 Регулятор ингредиентов."""

col_keksov = int(input("Введите кол-во кексовя:"))
sugar = ( 1.5 /  48 ) * col_keksov
oil = (1 / 48) * col_keksov
flour =(2.75 / 48) * col_keksov
print(f"Для кесов нам понадобится {sugar} стакана сахара,  {oil} стакана масла,  {flour} стакана муки")
