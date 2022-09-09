import random

user_wins = 0
computer_wins = 0
choice = ["papier", "caillou", "ciseaux"]

while True:
    user_input = input("Choisissez Papier, Caillou ou Ciseau ou Q pour quitter: ").lower()
    if user_input == "q":
        break

    if user_input not in choice:
        print("Votre choix n'est pas valide")
        continue

    random_number = random.randint(0, 2)
    computer_choice = choice[random_number]
    print("Choix de l'ordinateur", computer_choice + ".")

    if user_input == "caillou" and computer_choice == "ciseaux":
        print("Tu gagnes!")
        user_wins += 1

    elif user_input == "papier" and computer_choice == "caillou":
        print("Tu gagnes!")
        user_wins += 1

    elif user_input == "ciseaux" and computer_choice == "papier":
        print("Tu gagnes!")
        user_wins += 1
    elif user_input == computer_choice:
        print("Match nul!")
    else:
        print("Tu perds!")
        computer_wins += 1

print("Tu gagnes", user_wins, "fois.")
print("L'ordinateur gagne", computer_wins, "fois.")
print("Au revoir!")
