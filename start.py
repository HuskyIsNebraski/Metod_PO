def run_game(name, get_question_and_answer):
    print()
    rounds = 3

    for _ in range(rounds):
        question, correct_answer = get_question_and_answer()

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!\n")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!\n")
