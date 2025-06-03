# type_service.py
from flask import Flask, jsonify
import ast
from data_loader import load_pokemon_data

app = Flask(__name__)
data = load_pokemon_data()

@app.route("/get_by_type/<poke_type>")
def get_by_type(poke_type):
    poke_type = poke_type.strip().title()
    matching = []
    for row in data:
        types = ast.literal_eval(row["Type"])
        if poke_type in types:
            matching.append({"Name": row["Name"], "Type": types})
    return jsonify(matching)

if __name__ == "__main__":
    app.run(port=5003, debug=True)
