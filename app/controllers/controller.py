from app import app
from app.models.players import *
from flask import render_template, redirect


@app.route('/home')
def home_screen():
    return render_template("home_page.html")

@app.route('/input')
def input_screen():
    return render_template("player_input.html")


