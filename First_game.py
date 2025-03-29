import math
import random


def lcm(a, b, c):
    return math.lcm(a, b, c)


def play_game(name):
    print("Find the smallest common multiple of given numbers.\n")

    rounds = 3
    for _ in range(rounds):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm(*numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
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
