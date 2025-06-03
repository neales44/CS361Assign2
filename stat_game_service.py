# stat_service.py
from flask import Flask, jsonify
import random, ast
from data_loader import load_pokemon_data

app = Flask(__name__)
data = load_pokemon_data()

@app.route("/random_stat_game_prompt")
def stat_game_prompt():
    selected = random.choice(data)
    return jsonify({
        "HP": selected["HP"],
        "Attack": selected["Attack"],
        "Defense": selected["Defense"],
        "Type": ast.literal_eval(selected["Type"]),
        "CorrectAnswer": selected["Name"]
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)
