
from Dinosaur import dinosaur
from Weapon import weapon

class robot:
    def __init__(self):
        self.name = "Mega T8"
        self.health = 100
        self.active_weapon = (weapon)
        pass

    def attack(self,):
        self.active_weapon -= dinosaur.health
