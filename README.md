# Pokémon Microservice A – Stat Guessing Game Service

## Microservice Overview

This Flask based microservice serves stat based Pokémon guessing game prompts. It runs on port **5001** and returns randomized Pokémon stat lines and the correct answer in JSON format.

---

## How to Request and Receive Data

### Example Call (Python)
```python
import requests

response = requests.get("http://localhost:5001/random_stat_game_prompt")
data = response.json()
print(data)







Client          Stat Game Microservice
   |                    |
   |  GET /type_clue    |
   |------------------->|
   |                    |
   |     JSON Response  |
   |<-------------------|
   



//Stole template for this online