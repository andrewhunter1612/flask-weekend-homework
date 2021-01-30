class Game:
    def __init__(self):
        self.player_one_wins = 0
        self.player_two_wins = 0
        self.draws = 0
        self.number_of_games = 1
        self.human_players = 0
        self.winner = ""
        self.history = []
        self.player_one_weapon = ""
        self.player_two_weapon = ""

    def set_number_of_games(self, number_of_games):
        self.number_of_games = number_of_games

    def set_human_players(self, number_of_players):
        self.human_players = number_of_players

    def get_human_players(self):
        return self.human_players

    def get_possible_outcomes(self):
        outcomes = [
            {"name": "rock", "beats": "scissors", "loses": "paper"}, 
            {"name": "paper", "beats": "rock", "loses": "scissors"},
            {"name": "scissors", "beats": "paper", "loses": "rock"}
        ]
        return outcomes

    def set_player_weapons(self, player_one, player_two):
        self.player_one_weapon = player_one.choice 
        self.player_two_weapon = player_two.choice
    

    def start_game(self, player_one, player_two):
        outcomes = self.get_possible_outcomes()
    
        self.set_player_weapons(player_one, player_two)
        
        for outcome in outcomes:
            if outcome["name"] == self.player_one_weapon:
                if self.player_two_weapon == outcome["beats"]:
                    self.winner = "Player 1"
                    self.player_one_wins +=1

                elif self.player_two_weapon == outcome["loses"]:
                    self.winner = "Player 2"
                    self.player_two_wins +=1

                elif self.player_two_weapon == outcome["name"]:
                    self.winner = "Draw"
                    self.draws +=1

        self.history.append({"player_1": self.player_one_weapon, "player_2": self.player_two_weapon, "winner": self.winner})

        





