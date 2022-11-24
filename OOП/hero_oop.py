import random


class Unit:
    BALANS = 0
    withdrawn_money = 0
    LVL_HERO = 1
    XP_HERO = 0
    HP_HERO = 1000
    MANA_HERO = 200
    GOLD = 0
    SILVER = 1000
    PEARL = 0
    ATACA = 90
    MOB = 200
    FRAZY = ['И это удар?', 'СЕЙЧАС ПОКАЖУ ГДЕ РАКИ ..']

    SUMKA_HERO = []



class Donat(Unit):

    @classmethod
    def replenishment(cls, x):
        cls.BALANS += x

    @classmethod
    def bal_gol(cls, x):
        cls.BALANS -= x
        cls.withdrawn_money += x
        print("Со счета было снято: ", x)

    @classmethod
    def info_balans(cls):
        print('Счет баланса состовляет: ', cls.BALANS)

    @classmethod
    def withdrawn_mone(cls):
        print("Игровой счет состовляет : ", cls.withdrawn_money)


class Mob(Unit):
    MOB = 200

    @classmethod
    def ataca_mob(cls):

        a = cls.HP_HERO * 0.3
        cls.HP_HERO -= a

    @classmethod
    def hill(cls):
        cls.MOB += 50

    @classmethod
    def info_mob(cls):
        print('HP mob', cls.MOB)


class Hero(Mob,Donat):

    @classmethod
    def ataca_hero(cls):
        # super().ataca_mob()
        rand = random.choice(cls.FRAZY)

        if cls.MOB > 0:
            cls.MOB -= cls.ATACA
            if cls.MOB <= 180:
                print(rand)

        if cls.MOB < 0:
            cls.XP_HERO += 100
            cls.GOLD += 10
            print('я не мог... ')


    @classmethod
    def flasc(cls):

        cls.HP_HERO += 25

    @classmethod
    def clariti(cls):

        cls.MANA_HERO += 20

    @classmethod
    def fair(cls):

        cls.MOB -= 150
        if cls.MOB <= 1:
            print("Я еще вернусь")

        if cls.HP_HERO < 1000:
            cls.HP_HERO += 50

        if cls.MOB < 0:
            cls.XP_HERO += 100

    @classmethod
    def v(cls, v):
        cls.withdrawn_money -= v
        c = v / 10
        cls.GOLD += c

    @classmethod
    def info_hero(cls):

        print('HP Hero', cls.HP_HERO)
        print('XP', cls.XP_HERO)
        # print('GOOLD', cls.GOLD)
        # print('Mana: ',cls.MANA_HERO)

    @classmethod
    def shop(cls, i):
        cls.i = i
        if i == 'clar':
            cls.GOLD -= 1
            cls.SUMKA_HERO.append(i)
            print(cls.SUMKA_HERO)

        if i == 'man':
            cls.GOLD -= 1
            cls.SUMKA_HERO.append(i)
            print(cls.SUMKA_HERO)


    @classmethod
    def uze(cls,x = None,y = None):

        for o in cls.SUMKA_HERO:
            if  x == o:
                cls.HP_HERO += 20
                break



h = Hero()
m = Mob()
m.ataca_mob()
m.ataca_mob()
h.info_hero()
