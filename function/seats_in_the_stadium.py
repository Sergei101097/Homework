bn = []
def showIncome():
    global bn
    a = int(input("Enter count of A seats: "))
    b = int(input("Enter count of B seats: "))
    c = int(input("Enter count of C seats: "))
    aa(a)
    bb(b)
    cc(c)
    s(bn)
def aa (val):
    a = val * 10
    bn.append(a)
    print(f"Сумма проданных мест сектора 'A' составило {a} $")
def bb(val):
    b = val * 15
    bn.append(b)
    print(f"Сумма проданных мест сектора 'B' составило {b} $")
def cc (val):
    c = val * 20
    bn.append(c)
    print(f"Сумма проданных мест сектора 'C' составило {c} $")

def s(vak):
    total = sum(vak)
    print(f"Общая сумма  проданных мест составила {total} $")

showIncome()
