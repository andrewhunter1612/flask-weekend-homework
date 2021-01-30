import random

class Player:
    def __init__(self):
        self.human = False
        self.choice = ""


    def set_player_choice(self, human, choice):
        if human:
            self.choice = choice
        else:
            choice = ["rock", "paper", "scissors"]
            self.choice = [random.randrange(0,2)]

    def set_human_player(self, human):
        self.human = human

    def get_player_choice(self):
        return self.choice

    def check_if_player_is_human(self):
        return self.human

 


