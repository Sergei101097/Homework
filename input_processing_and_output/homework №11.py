"""Задача № 11 Программа расчета купли-продажи акций."""

stock = int(input("Введите кол-во акций:"))

share_price = float(input("Введите цену акции:"))

broker_commission = float(input("Введите % брокера:"))

sold_shares = int(input("Введите кол-во продоваемых акций:"))

selling_price = float(input("Введите цену продоваемой акции:"))

broker_commission_1 = float(input("Введите % брокера:"))


total_prace_stock = stock * share_price
commission = (total_prace_stock * broker_commission) / 100
total = total_prace_stock + commission


sale = sold_shares * selling_price
commission_1 = (sale * broker_commission_1) / 100
total_1 = sale - commission_1

profit_or_loss = total_1 - total

print(f"За  {stock} акции  сумма составила  {total_prace_stock} $\nУслуги брокера обошлись вам в {commission} $\nCумма покупки составила {total} $")

print(f"Вы продали  {sold_shares} акции  сумма составила {sale} $\nУслуги брокера обошлись вам в {commission_1} $\nВы продали акции на  {total_1} $")

if profit_or_loss >= 0 :
     print( f"Прибыль составла {profit_or_loss}")
else:
    print(f"Убыток составил {profit_or_loss}")


"""Задание №12 Выращивание виноrрада."""