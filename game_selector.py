import First_game
import Second_game


def choose_game():
    print("Please choose a game:")
    print(f"1. {First_game.DESCRIPTION}")
    print(f"2. {Second_game.DESCRIPTION}")
    choice = input("Enter 1 or 2: ")

    while choice not in ('1', '2'):
        choice = input("Invalid choice. Please enter 1 or 2: ")

    return int(choice)
