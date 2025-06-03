# name_service.py
from flask import Flask, jsonify
from data_loader import load_pokemon_data

app = Flask(__name__)
data = load_pokemon_data()

@app.route("/get_by_name/<name>")
def get_by_name(name):
    name = name.strip().lower()
    for row in data:
        if row["Name"].strip().lower() == name:
            return jsonify(row)
    return jsonify({"error": f"No Pokémon found with name '{name}'."})

if __name__ == "__main__":
    app.run(port=5004, debug=True)
