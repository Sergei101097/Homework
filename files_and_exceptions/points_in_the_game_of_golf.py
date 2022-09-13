def total_game_golf():
    global bal_name_game_1,bal_name_game_2
    bal_name_game_1 = []
    bal_name_game_2 = []
    i = int(input("Введите количеество раундов: "))
    name_1 = str(input("name №1 game: "))
    name_2 = str(input("name №2 game: "))
    ernp_file = open('ernployees.txt','w')
    ernp_file.write(name_1 + '\t'+'\t'+'\t'+'\t'+'\t'+'\t'+name_2)
    bal_game(i,name_1,name_2,ernp_file)
    sum_ball_game(ernp_file,name_1,name_2)

def bal_game(bal,name_1,name_2,ernp_file):
    for count in range(1, bal + 1):
        bal = int(input(f"bal {name_1}: "))
        bal_1 = int(input(f"bal {name_2}: "))
        bal_name_game_1.append(bal)
        bal_name_game_2.append(bal_1)
        ernp_file.write('\n' + str(bal) + '\t'+'\t'+'\t'+'\t'+'\t'+'\t'+'\t'+ str(bal_1))
def sum_ball_game(ernp_file,name_1,name_2):

    x = list(map(int, bal_name_game_1))
    v = sum(x)
    xx = list(map(int, bal_name_game_2))
    vv = sum(xx)
    ernp_file.write('\n'+'\n' +f"Итого: {str(v)} балла" + '\t' +'\t'+'\t'+ f"Итого: {str(vv)} былла")
    if v < vv:
        ernp_file.write("\n" + f"Игрок {name_2} победил")
    else:
        ernp_file.write("\n" + f"Игрок {name_1}  победил")
total_game_golf()





def na():
    total = open("ernployees.txt", "r")
    g = total.read()
    print(g)
na()





























# def nai():
#
#     b = int(input("kil game name: "))
#     ernp_file = open('ernployeesss.txt', 'w')
#     for i in range(1,b+1):
#         name_1 = str(input("name game: "))
#         ernp_file.write(name_1 + '\n')
#
#
# nai()
