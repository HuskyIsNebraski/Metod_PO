import random


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(1, length - 2)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = ' '.join(map(str, progression))
    return question, correct_answer


DESCRIPTION = "What number is missing in the progression?"
