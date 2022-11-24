# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#
#     def __init__(self,x,y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#
#             self.x = x
#             self.y = y
#
#     def get_coords(self):
#         return  self.x, self.y
#
# pt = Point(1,2)
#
#
#
# f = 100
# g = 0
#
# i = int(input("число: "))
#
# f -= i
#
# g+=i
# print(f)
# print(g)

class Student():

    def __init__(self,name,grup,bal):

        self.name = name
        self.grup = grup
        self.bal = bal

    def grad (self):

        return  self.bal

class Schol():

    def __init__(self,name,max_bal):

        self.name = name
        self.max_bal = max_bal
        self.vit = []

    def app_stude(self,student):

        self.vit.append(student)

    def  sred(self):
        value = 0
        for srudi in self.vit:
            value += srudi.grad()

        return  value / len(self.vit)



s = Student('ser',2,56)
s1 = Student('dim',2,59)
s2 = Student('mih',2,60)

Sc = Schol('it',3)

Sc.app_stude(s)
Sc.app_stude(s1)
Sc.app_stude(s2)
print(Sc.sred())



























