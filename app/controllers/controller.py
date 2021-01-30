from app import app
from flask import render_template, redirect, request
from app.models.player import *
from app.models.game import *


@app.route('/home')
def home_screen():
    return render_template("home_page.html")

@app.route('/home', methods=["POST"])
def choose_number_of_players():
    game = Game()
    game.set_human_players(request.form['number_of_players'])
    number_of_players = game.get_human_players()
    player_one = Player()
    player_two = Player()
    for _ in range(3):
        if number_of_players == 1:
            player_one = Player(True, "")
        elif number_of_players == 2:
            player_one = Player(True, "")
            player_two = Player(True, "")
    return redirect('/input')

    @app.route('/input')
    def input_screen():
        game = Game()
        number_of_humans = game.get_human_players()
        return render_template("player_input.html", players=number_of_humans)


