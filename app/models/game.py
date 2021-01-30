class Game:
    def __init__(self):
        self.player_one_wins = 0
        self.player_two_wins = 0
        self.draws = 0
        self.number_of_games = 1
        self.human_players = 0

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

    

    def start_game(self, player_one, player_two):
        outcomes = self.get_possible_outcomes()
        

        for _ in range(self.number_of_games):
            if number_of_players == 0:
                player_one = player_one.get_computer_choice()
                player_two = player_two.get_computer_choice()
            elif number_of_players ==1:
                player_one = player_one.get_computer_choice()
                player_two = return_random_decision(random.randrange(0,2))
            elif number_of_players ==2:
                player_one = input("Player 1: enter rock, paper or scissors: ")
                player_two = input("Player 2: enter rock, paper or scissors: ")
            else:
                number_of_players = input("Enter the number of players: ")

            for outcome in outcomes:
                if outcome["name"] == player_one:
                    if player_two == outcome["beats"]:
                        player_one_wins += 1
                        print("player one wins")
                    elif player_two == outcome["loses"]:
                        player_two_wins += 1
                        print("player two wins")
                    elif player_two == outcome["name"]:
                        draws += 1
        





