
from Robot import robot

class dinosaur:
    def __init__(self):
        self.name = "Beastasouraus Rex"
        self.health = 100
        self.attack_power = 20
        pass

    def attack(self):
        self.attack_power -= robot.health