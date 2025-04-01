from First_game import (
    DESCRIPTION as first_description,
    get_question_and_answer as first_question,
)
from Second_game import (
    DESCRIPTION as second_description,
    get_question_and_answer as second_question,
)
from game_selector import choose_game
from start import run_game


def main():
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")

    game = choose_game()
    print()

    if game == 1:
        print(first_description)
        run_game(name, first_question)
    else:
        print(second_description)
        run_game(name, second_question)


if __name__ == "__main__":
    main()
