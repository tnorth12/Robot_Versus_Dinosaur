# Import robot and dinosaur

from Robot import robot
from Dinosaur import dinosaur
from Weapon import weapon

# Declare the Battlefield class

class battlefield:
    def __init__(self):
        self.name = "Battlefield One"
        pass
        

    def run_game(self):
        self.greeting()
        self.battle_phase()
        self.display_winner()
        
        
        
            

                   
        pass

    def greeting(self):                             #why wouldn't it import dino and robot names?
        print("""
        
Welcome to the Battlefield! The battle between robot and dinosaur is about to begin!!                          

    """ )


    def battle_phase(self):  
        robot.robo_health = 100    
        weapon.robo_destroy = 15
        dinosaur.thunder_punch = 20
        dinosaur.dino_health = 100
        while dinosaur.dino_health and robot.robo_health > 0:
            dinosaur.dino_health -= weapon.robo_destroy
            print(f"\nWhat a shot by the robot!!\nDinosaur health is reduced to {dinosaur.dino_health} after that attack!!\n")
            pass
            robot.robo_health -= dinosaur.thunder_punch 
            print(f"\nAn awesome blow by the donosaur!!\nRobot health is reduced to {robot.robo_health} now!!\n")
            

        if dinosaur.dino_health <= 0:
            print(
                
"""Down goes the Dino!!"""
)
            return battlefield.battle_phase
            
            
        if robot.robo_health <= 0:
            print(

"""The Robot is out!!"""
)
            return battlefield.battle_phase
            
                
            # robo_attack_dino(dinosaur)
            #     subtract health on attack
            # dino_attack_robo(robot)
            #     subtract health on attack

    def display_winner():
        print(f"display {battlefield.battle_phase}")
        
