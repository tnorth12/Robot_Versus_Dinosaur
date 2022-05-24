


from Weapon import weapon

class robot:
    def __init__(self, robo_health):
        self.name = "Mega T8"
        self.robot_health = robo_health
        
        pass

    def robo_attack(self, robo_destroy):
        weapon.attack_power = robo_destroy
