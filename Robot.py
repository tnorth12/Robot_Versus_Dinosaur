

from Dinosaur import dinosaur
from Weapon import weapon

class robot:
    def __init__(self, robo_health, robo_destroy):
        self.name = "Mega T8"
        self.health = robo_health
        weapon.attack_power = robo_destroy
        pass

    def attack(self):
        self.active_weapon -= dinosaur.health
