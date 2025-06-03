Pokémon Microservice – Type Clue Guessing Game
1. How to REQUEST Data
This microservice listens on http://localhost:5002/random_clue_game_prompt.
It returns a JSON response with 3 clues to guess the name of a Pokémon.

Example (using Python and the requests library): python import requests

response = requests.get("http://localhost:5002/random_clue_game_prompt") data = response.json()

print("First type clue:", data["FirstType"]) print("Second type clue:", data["SecondType"]) print("First letter of name:", data["FirstLetter"]) print("Correct answer (for testing):", data["CorrectAnswer"])

You can use this data to prompt the user for guesses based on the type and name clues.

2. How to RECEIVE Data
After calling the endpoint, the microservice responds with a JSON object containing:

FirstType: The Pokémon's primary type.
SecondType: The secondary type, or None if there isn't one.
FirstLetter: The first letter of the Pokémon's name.
CorrectAnswer: The actual name of the Pokémon (used to check guesses).
Example response: json { "FirstType": "Water", "SecondType": "Flying", "FirstLetter": "G", "CorrectAnswer": "Gyarados" }

You can build a game interface by showing one clue at a time and checking the user’s guess after each.

Microservice Overview
This Flask-based microservice serves type-based Pokémon guessing game prompts. It runs on port 5002 and returns randomized Pokémon clue data in JSON format.

Example Call
python import requests

response = requests.get("http://localhost:5002/random_clue_game_prompt") data = response.json() print(data)

Client Type Clue Game Microservice
| |
| GET /random_clue_game_prompt |
|----------------------------->|
| |
| JSON Response |
|<-----------------------------|
