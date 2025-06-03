# clue_service.py
from flask import Flask, jsonify
import random, ast
from data_loader import load_pokemon_data

app = Flask(__name__)
data = load_pokemon_data()

@app.route("/random_clue_game_prompt")
def clue_game_prompt():
    selected = random.choice(data)
    types = ast.literal_eval(selected["Type"])
    return jsonify({
        "FirstType": types[0],
        "SecondType": types[1] if len(types) > 1 else None,
        "FirstLetter": selected["Name"][0],
        "CorrectAnswer": selected["Name"]
    })

if __name__ == "__main__":
    app.run(port=5002, debug=True)
