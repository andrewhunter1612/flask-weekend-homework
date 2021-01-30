from app import app
from flask import render_template, redirect, request
from app.models.player import *
from app.models.game import Game
from app.models.set_up_game import game, player_one, player_two

def set_up():
    game = Game()
    player_one = Player()
    player_two = Player()

@app.route('/')
def home_screen():
    return render_template("home_page.html")

@app.route('/', methods=["POST"])
def choose_number_of_players():
    game.set_human_players(request.form['number_of_players'])
    number_of_players = game.get_human_players()
    if number_of_players == "1":
        player_one.human = True
    elif number_of_players == "2":
        player_one.human = True
        player_two.human = True

    return redirect('/input')

@app.route('/player-input', methods=["POST"])
def set_player_input():
    player_one.set_player_choice(player_one.human, request.form['player_one'])
    player_two.set_player_choice(player_two.human, request.form['player_two'])
    game.start_game(player_one, player_two)

    return redirect("/results")

@app.route('/results')
def results_screen():
    return render_template("results.html", title="Results", game=game)

@app.route('/input')
def input_screen():
    return render_template("player_input.html", players=game)


