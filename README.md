# CS361 Assignment 2: Pokémon Clue Game Microservice
This project implements a Pokémon-themed microservice architecture where the main service generates a clue-based guessing game. Supporting services provide Pokémon names, types, and stat data, and communicate via RESTful HTTP APIs.

## Repository Structure
- clue_game_service.py: Main microservice that provides the clue-based game
- name_service.py: Provides a random Pokémon name
- type_service.py: Provides types for a given Pokémon
- stat_game_service.py: Provides stats for a potential stat-guessing game
- client.py: Sample client for the clue service
- test_client_type_clue.py: Unit test for the clue service
- data_loader.py: Loads and parses the Pokémon dataset
- pokePd.csv: Dataset of Pokémon
- requirements.txt: Python dependencies

## How to Run the Full Microservice Suite
It's best to run each microservice in its own terminal window.

### 1. Clone and Set Up the Project
git clone https://github.com/neales44/CS361Assign2.git
cd CS361Assign2
python3 -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
pip install -r requirements.txt


If requirements.txt is missing, install manually:
pip install flask requests



### 2. Start the Supporting Microservices

#### Run name_service.py
python name_service.py


- Runs on: http://localhost:5001
- Endpoint: /random_name

#### Run type_service.py
python type_service.py


- Runs on: http://localhost:5003
- Endpoint: /get_types/<pokemon_name>

#### Optional: Run stat_game_service.py
python stat_game_service.py


- Runs on: http://localhost:5004
- Endpoint: /get_stat_prompt
- This is for a potential future stat-guessing game

### 3. Run the Main Clue Game Service
python clue_game_service.py


- Runs on: http://localhost:5002
- Endpoint: /random_clue_game_prompt
- This service fetches a Pokémon name from name_service and its types from type_service, then returns a clue in JSON format like:
{
"FirstType": "Fire",
"SecondType": "Flying",
"FirstLetter": "C",
"Answer": "Charizard"
}



## Testing
To test the clue game manually:
python client.py


To run the automated unit test:
python test_client_type_clue.py



## Example Flow
1. clue_game_service.py calls name_service.py to get a random Pokémon name.
2. It then calls type_service.py to retrieve the type(s) of that Pokémon.
3. clue_game_service.py returns a JSON clue containing the first type, second type (or "None"), the first letter of the name, and the full answer.

## Requirements
- Python 3.7+
- Flask
- requests

