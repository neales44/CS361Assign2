import requests

def show_main_menu():
    print("\nMain Menu:")
    print("1. Go to Pokédex")
    print("2. Play Stat Guessing Game")
    print("3. Play Type Clue Guessing Game")
    print("4. Exit")

def show_pokedex_menu():
    print("\n Pokédex Menu:")
    print("1. View All Pokémon (not implemented)")
    print("2. Search by Type")
    print("3. Search by Name")
    print("4. Back to Main Menu")

def stat_game():
    score = 0
    for round_num in range(1, 6):
        res = requests.get("http://localhost:5001/random_stat_game_prompt").json()
        correct = res["CorrectAnswer"]
        options = [correct]

        # Get 3 other Pokémon names as distractors
        while len(options) < 4:
            poke = requests.get("http://localhost:5004/get_by_name/" + correct).json()
            rand_poke = requests.get("http://localhost:5001/random_stat_game_prompt").json()
            if rand_poke["CorrectAnswer"] not in options:
                options.append(rand_poke["CorrectAnswer"])

        import random
        random.shuffle(options)

        print(f"\nRound {round_num}:")
        print(f"Stat Line: HP: {res['HP']}, Attack: {res['Attack']}, Defense: {res['Defense']}")
        print(f"Type(s): {res['Type']}")
        for i, opt in enumerate(options):
            print(f"{i + 1}. {opt}")

        try:
            guess = int(input("Enter your guess (1-4): "))
            if options[guess - 1].lower() == correct.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. It was {correct}.")
        except:
            print("Invalid input.")

    print(f"\nGame Over! Your score is: {score}/5")

def type_clue_game():
    res = requests.get("http://localhost:5002/random_clue_game_prompt").json()
    correct = res["CorrectAnswer"]

    print(f"\nClue 1: First type is {res['FirstType']}")
    guess = input("Your guess: ").strip().lower()
    if guess == correct.lower():
        print(f"Correct! The Pokémon was {correct}.")
        return

    print(f"\nClue 2: {'Second type is ' + res['SecondType'] if res['SecondType'] else 'No second type.'}")
    guess = input("Your guess: ").strip().lower()
    if guess == correct.lower():
        print(f"Correct! The Pokémon was {correct}.")
        return

    print(f"\nClue 3: Pokémon starts with '{res['FirstLetter']}'")
    guess = input("Final guess: ").strip().lower()
    if guess == correct.lower():
        print(f"Correct! The Pokémon was {correct}.")
    else:
        print(f"Out of guesses. It was {correct}.")

def pokedex_search():
    while True:
        show_pokedex_menu()
        choice = input("Choice: ").strip()
        if choice == '1':
            print("View All not implemented in microservices version.")
        elif choice == '2':
            poke_type = input("Enter type: ")
            res = requests.get(f"http://localhost:5003/get_by_type/{poke_type}").json()
            if res:
                for poke in res:
                    print(f"{poke['Name']} - {poke['Type']}")
            else:
                print(f"No Pokémon found with type '{poke_type}'.")
        elif choice == '3':
            name = input("Enter name: ")
            res = requests.get(f"http://localhost:5004/get_by_name/{name}").json()
            if 'error' in res:
                print(res['error'])
            else:
                for k, v in res.items():
                    print(f"{k}: {v}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def main():
# print(" Welcome to the Pokémon Terminal App!")
    while True:
       # show_main_menu()
        choice = input("Enter 3 to start: ").strip()
        if choice == '1':
            pokedex_search()
        elif choice == '2':
            stat_game()
        elif choice == '3':
            type_clue_game()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
