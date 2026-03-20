# class Hero:
#
#     #Конструктор класса
#     def __init__(self,name, lvl, hp):
#         #Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
# #Экзкмпляр/Объектом на основе класса
# kirito = Hero("kirito",100,1000)
# aman = Hero("")
# MageHero
# mage_hero

# Родительский\Супер класс
class Hero:

    # Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def action(self):
        print(f"{self.name} base action!!")

    # Принт
    def __str__(self):
        return self.name

# Экземпляр\Объектом на основе класса
kirito = Hero("Kirito")
asuna = Hero("Asuna")
kirito.action()


# Дочерний класс
class MageHero(Hero):

    def cast_spell(self):
        print(f"{self.name} cass fire!!")

gendalf = MageHero("Gendalf")


# gendalf.cast_spell()
# asuna.action()