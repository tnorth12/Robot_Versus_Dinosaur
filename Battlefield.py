# Import Fleet and Herd


from ast import Return
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
        print("Battle start")
        self.indentify_winner()
        pass

    def greeting(self):
        print("""
        
Welcome to the Battlefield! Dino and Robot attack!

    """ )



    def battle_phase(self):  
        dino_health = 100
        robo_health = 100   
        thunder_punch = 20
        robo_destroy = 15
        while dino_health and robo_health > 0:
            robo_health -= thunder_punch
            print(f"Robot health is reduced to {robo_health} after that attack")
            pass
            dino_health -= robo_destroy
            print(f"Dinosaur health is reduced to {dino_health} after that attack")
        if dino_health <= 0:
            print("Down goes the Dino!!")
            winner = dinosaur
            return winner 
            
        if robo_health <= 0:
            print("The Robot is out!!")
            winner = robot
            return winner 
            
                
            # robo_attack_dino(dinosaur)
            #     subtract health on attack
            # dino_attack_robo(robot)
            #     subtract health on attack

    def indentify_winner(self, winner):
        self.winner = winner
