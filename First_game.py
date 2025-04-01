import math
import random


def get_question_and_answer():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = ' '.join(map(str, numbers))
    answer = math.lcm(*numbers)
    return question, answer


DESCRIPTION = "Find the smallest common multiple of given numbers."
