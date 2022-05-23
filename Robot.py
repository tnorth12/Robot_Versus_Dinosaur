

from Dinosaur import dinosaur
from Weapon import weapon

class robot:
    def __init__(self, robo_health):
        self.name = "Mega T8"
        self.health = robo_health
        self.active_weapon = (weapon.attack_power)
        pass

    def attack(self):
        self.active_weapon -= dinosaur.health
