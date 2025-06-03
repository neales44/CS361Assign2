# data_loader.py
import csv

def load_pokemon_data(filename="pokePd.csv"):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))
