from random import randint

from abstract_classes import FighterAbstract #Import class from file
from abstract_classes import ContestAbstract #Import class from file

class Fighter(FighterAbstract):

    def __str__(self):
        return f'Я - {self.name} c характеристиками (❤, 🛡, ⚔): {self.health, self.armor, self.strength}'

    def __init__(self, name, health, strength, armor): #new constructor
        super().__init__(name) #parent's constructor use
        self.health = health
        self.armor = armor
        self.strength = strength

    def attack(self):
        critical_damage = randint(1, 2)

        if critical_damage == 2:
            print("Наношу критический удар c силой в 2 раза больше обычного!")
        else:
            print("Наношу обычный удар.")

        return (self.strength * critical_damage)

    def get_damage(self, damage):
        parry = randint(0, 1)

        if parry == 0:
            print("Парировал удар. Урона не будет!")
        else:
            print("Получил урон = " + str(damage))

        self.health -= damage * parry


class Contest(ContestAbstract):

    def meet_fighters(cls, player1, player2):
        print("Приветствуйте бойцов!")
        print(player1)
        print(player2)
        print("\n\n\n")

    def start_battle(cls, player1, player2):

        who_attacks = randint(1, 2)
        print("Первым атаковать будет игрок № = " + str(who_attacks))
        print("Битва началась!")

        if who_attacks == 1:
            player2.get_damage(player1.attack())
            

        while True:       
            player1.get_damage(player2.attack())
            if player1.health <= 0:
                print("Игрок 2 победил!")
                break

            player2.get_damage(player1.attack())
            if player2.health <= 0:
                print("Игрок 1 победил!")
                break
