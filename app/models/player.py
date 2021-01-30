import random

class Player:
    def __init__(self):
        self.human = False
        self.choice = ""


    def set_player_choice(self, human, chosen):
        if human:
            self.choice = chosen
        else:
            choice = ("rock", "paper", "scissors")
            decided = choice[random.randrange(0,2)]
            self.choice = decided

    def set_human_player(self, human):
        self.human = human

    def get_player_choice(self):
        return self.choice

    def check_if_player_is_human(self):
        return self.human

 


