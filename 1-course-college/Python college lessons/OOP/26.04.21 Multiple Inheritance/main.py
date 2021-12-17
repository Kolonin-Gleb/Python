#Multiple Inheritance

class Wizard:
    def __init__(self, magic_stick, coat):
        self.magic_stick = magic_stick
        self.coat = coat

    def cast_spell(self):
        print('Fireball')

    def talk(self):
        print('I am too old')

class Warior:
    def __init__(self, weapon, shield):
        self.weapon = weapon
        self.shield = shield

    def hit(self):
        print("zzzz")

    def talk(self):
        print('For Soviet Union!')

class Creature():
    def __init__(self, health, speed, mana, money, damage):
        self.health = health
        self.speed = speed
        self.mana = mana
        self.money = money
        self.damage = damage

class WariorWizard(Creature, Warior, Wizard): #1 class is more important than 2 class in brackets
    count = 0

    def __init__(self, health, speed, mana, money, damage, weapon, shield:str, magic_stick, coat:bool):
        Creature.__init__(self, health, speed, mana, money, damage)
        Warior.__init__(self, weapon, shield)
        Wizard.__init__(self, magic_stick, coat)
        WariorWizard.count += 1
        
    def talk(self):
        Wizard.talk(self)
        Warior.talk(self)

    #static method
    @staticmethod
    def stat():
        print("static method")

    #method to work with class not with objects
    @classmethod
    def print_count(cls): #cls - class
        print(f'Total count = {cls.count}')



player = WariorWizard(300, 50, 200, 0, 150, 'sword', False, True, True)
player2 = WariorWizard(3030, 530, 2300, 30, 1350, 'knife', True, True, True)
# print(player)
# player.cast_spell()
# player.hit()
# player.talk()

# print(WariorWizard.mro()) #Show class priorities

#call static method
# player.stat()
# WariorWizard.stat()

# call class method
player.print_count()
WariorWizard.print_count()
