# Import Fleet and Herd

from Fleet import fleet
from Herd import herd

from Robot import robot
from Dinosaur import dinosaur

# Declare the Battlefield class

class battlefield:
    def __init__(self):
        self.fleet_robots = fleet("Robo T4s")
        self.herd_dinosaurs = herd("Attack Dinos")
        # self.name = "Battlefield One"
        pass

    def run_game(self):
        self.greeting()
        #run_battle()
        #while dino.hp and robo.hp is greater than 0
            #robo_attack_dino(dinosaur)
                # subtract health on attack
            #dino_attack_robo(robot)
                # subtract health on attack
        print("Battle start")
        self.ending()
        pass

    def greeting(self):
        print("""
        
Welcome to the Battlefield! Dino and Robot attack!

    """ )

    def battle_start(self)          #Maybe attack portion

    def indentify_winner(self):


    def ending(self):
        print("""

I hope you enjoyed the carnage!"""
    )