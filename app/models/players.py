import random

class Players:
    def __init__(self, human, choice):
        self.human = human
        self.choice = choice


    def get_computer_choice(self):
        choice = ["rock", "paper", "scissors"]
        return choice[random.randrange(0,2)]

    def get_player_choice(self, choice):
        return choice

 


