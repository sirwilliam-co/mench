
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
players = ["red", "green", "blue", "yellow"]
positions = {player: 0 for player in players}
turn_index = 0
last_roll = 1
MAX_CELLS = 40

@app.route("/")
def index():
    player = request.args.get("player")
    if player not in players:
        return "لطفاً آدرس را با پارامتر ?player=red باز کنید", 400

    current_turn = players[turn_index]
    return render_template("index_multi.html",
                           player=player,
                           current_turn=current_turn,
                           positions=positions,
                           last_roll=last_roll,
                           max_cells=MAX_CELLS)

@app.route("/roll", methods=["POST"])
def roll():
    global turn_index, last_roll
    player = request.form["player"]
    if player != players[turn_index]:
        return redirect(url_for("index", player=player))
    dice = random.randint(1, 6)
    last_roll = dice
    positions[player] += dice
    if positions[player] >= MAX_CELLS:
        positions[player] = MAX_CELLS - 1
    turn_index = (turn_index + 1) % len(players)
    return redirect(url_for("index", player=player))

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
