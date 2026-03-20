# class user:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name_age (self):
#         return f"{self.name, self.age}"
#
# name_age = user("nurahim",16)
# print(name_age.name_age)
class Bank:
    def __init__(self,name, profil, balans, curs):
        self.name = name
        self.profil = profil
        self.balans = balans
        self.curs = curs
    def hello_name(self):
        print(f"{self.name} Как дела у тебя")

    def action(self):
        print(f"{self.balans} $  У тебя столко денег")

    def buting (self):
        print(f"{self.curs} 1долар в сомах 87сом у тебя 1000долар 87000сом")

    def acount(self):
        print(f"{self.profil} Это твой профиль добро пожаловать")

Nurahim = Bank("Nurahim", "nura2009",1000,100)
Nurahim.hello_name()
Nurahim.buting()
Nurahim.acount()
Nurahim.action()