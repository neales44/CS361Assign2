import csv
import ast
import random

# Load Pokémon data
def load_pokemon_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# Pokédex Features
def view_all(data):
    return "\n".join(f"{row['Name']} - {row['Type']}" for row in data)

def search_by_name(name, data):
    name = name.strip().lower()
    for row in data:
        if row['Name'].strip().lower() == name:
            return f"\nStats for '{row['Name']}':\n" + "\n".join(f"{key}: {value}" for key, value in row.items())
    return f"No Pokémon found with name '{name}'."

def search_by_type(poke_type, data):
    poke_type = poke_type.strip().title()
    matching = []
    for row in data:
        types = ast.literal_eval(row['Type'])
        if poke_type in types:
            matching.append(f"{row['Name']} - {row['Type']}")
    if matching:
        return f"\nPokémon with type '{poke_type}':\n" + "\n".join(matching)
    return f"No Pokémon found with type '{poke_type}'."

# Stat Guessing Game
def stat_guessing_game(data):
    score = 0
    print("\n  Stat Guessing Game!")
    
    for round_num in range(1, 6):
        selected_pokemon = random.choice(data)
        correct_name = selected_pokemon['Name']
        hp = selected_pokemon['HP']
        attack = selected_pokemon['Attack']
        defense = selected_pokemon['Defense']
        types = ast.literal_eval(selected_pokemon['Type'])

        print(f"\nRound {round_num}:")
        print(f"Stat Line: HP: {hp}, Attack: {attack}, Defense: {defense}")
        print(f"Type(s): {types}")

        # Randomly select 3 other Pokémon as options
        options = [selected_pokemon]
        while len(options) < 4:
            option = random.choice(data)
            if option not in options:
                options.append(option)

        # Shuffle the options to randomize their order
        random.shuffle(options)

        print("\nChoose the correct Pokémon:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option['Name']}")

        # Get the user's guess
        try:
            user_guess = int(input("Enter the number corresponding to your guess: "))
            if options[user_guess - 1]['Name'].lower() == correct_name.lower():
                print(f"Correct! The Pokémon was {correct_name}.")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_name}.")
        except (ValueError, IndexError):
            print("Invalid input. Please select a number between 1 and 4.")
    
    print(f"\nGame Over! Your score is: {score}/5")

# Main Program
def main():
    data = load_pokemon_data("pokePd.csv")
    print(" Welcome to the Pokémon Terminal App!")

    while True:
        print("\nMain Menu:")
        print("1. Go to Pokédex")
        print("2. Play Stat Guessing Game")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == '1':
            while True:
                print("\n Pokédex Menu:")
                print("1. View All Pokémon")
                print("2. Search by Type")
                print("3. Search by Name")
                print("4. Back to Main Menu")
                sub_choice = input("Enter 1, 2, 3, or 4: ").strip()

                if sub_choice == '1':
                    print("\nAll Pokémon:\n" + view_all(data))
                elif sub_choice == '2':
                    poke_type = input("Enter Pokémon type: ")
                    print(search_by_type(poke_type, data))
                elif sub_choice == '3':
                    name = input("Enter Pokémon name: ")
                    print(search_by_name(name, data))
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid option.")
        elif choice == '2':
            stat_guessing_game(data)
        elif choice == '3':
            print(" Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

