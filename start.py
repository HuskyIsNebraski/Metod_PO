from First_game import play_game as play_first_game
from Second_game import play_game as play_second_game


def choose_game():
    print("Please choose a game:")
    print("1. Find the Least Common Multiple of 3 numbers")
    print("2. Find the missing number in the progression")
    choice = input("Enter 1 or 2: ")

    while choice not in ('1', '2'):
        choice = input("Invalid choice. Please enter 1 or 2: ")

    return int(choice)


def main():
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")

    game_choice = choose_game()
    print()

    if game_choice == 1:
        play_first_game(name)
    elif game_choice == 2:
        play_second_game(name)


if __name__ == "__main__":
    main()
