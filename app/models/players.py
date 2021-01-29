import random

class Players:
    def __init__(self, number_of_human_players):
        self.number_of_human_players = number_of_human_players

    def computer_choice(self):
        choice = ["rock", "paper", "scissors"]
        print(choice[random.randrange(0,2)])


 


