import random

QUIZ_FILE = 'quiz.txt'

# load quiz questions
def load_quiz(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return [line.strip().split("|") for line in lines if line.strip()]
    except FileNotFoundError:
        print("Quiz file not found! please ensure the file exists.")
        return []


def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    for question, *options, correct in questions:
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Your answer (enter the option number): "))
                if 1 <= answer <= len(options):
                    break
                else:
                    print(f"please choose a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. please enter a number.")
        if options[answer - 1] == correct:
            print("correct!")
            score += 1
        else:
            print(f"wrong! the correct answer was: {correct}")
    print(f"\nYou scored {score}/{len(questions)}")

def main():
    print("Welcome to the quiz game!")
    questions = load_quiz(QUIZ_FILE)
    if not questions:
        return

    while True:
        run_quiz(questions)
        replay = input("\nDo you want to retake the quiz? (yes/no)").strip().lower()
        if replay not in ("yes",'y'):
            print("thank you for playing! goodbye!")
            break

if __name__=="__main__":
    main()