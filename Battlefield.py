# Import robot and dinosaur

from Robot import robot
from Dinosaur import dinosaur

# Declare the Battlefield class

class battlefield:
    def __init__(self):
        self.name = "Battlefield One"
        pass
        

    def run_game(self):
        self.greeting()
        self.battle_phase()  
        self.display_winner()
        print(f"\nToday's winner is {battlefield.battle_phase}!!")
        
            

                   
        pass

    def greeting(self):                             #why wouldn't it import dino and robot names?
        print("""
        
Welcome to the Battlefield! The battle between robot and dinosaur is about to begin!!                          

    """ )



    def battle_phase(self):  
        dino_health = 100
        robo_health = 100   
        thunder_punch = 20
        robo_destroy = 15
        while dino_health and robo_health > 0:
            dino_health -= robo_destroy
            print(f"\nWhat a shot by the robot!!\nDinosaur health is reduced to {dino_health} after that attack!!\n")
            pass
            robo_health -= thunder_punch
            print(f"\nAn awesome blow by the donosaur!!\nRobot health is reduced to {robo_health} now!!\n")
            

        if dino_health <= 0:
            print(
                
"""Down goes the Dino!!"""
)
            display_winner = "Robot"
            return display_winner
            
        if robo_health <= 0:
            print(

"""The Robot is out!!"""
)
            display_winner = "Dinosaur"
            return display_winner 
            pass
                
            # robo_attack_dino(dinosaur)
            #     subtract health on attack
            # dino_attack_robo(robot)
            #     subtract health on attack

    def display_winner():
        battlefield.battle_phase = ""
        
