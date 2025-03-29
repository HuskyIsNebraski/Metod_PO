import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(1, length - 2)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer


def play_game(name):
    print("What number is missing in the progression?\n")

    rounds = 3
    for _ in range(rounds):
        progression, correct_answer = generate_progression()

        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!\n")
