# Import Fleet and Herd


from Robot import robot
from Dinosaur import dinosaur

# Declare the Battlefield class

class battlefield:
    def __init__(self):
        self.robot_warrior = (robot)
        self.dino_warrior = (dinosaur)
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
    
        while dinosaur.health and robot.health > 0:
            if dinosaur.attack():
                print(f"Robot health is reduced to {robot.health} after that attack")
            pass
            # robo_attack_dino(dinosaur)
            #     subtract health on attack
            # dino_attack_robo(robot)
            #     subtract health on attack

    def indentify_winner(self, winner):
        self.winner = winner
