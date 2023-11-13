import random

def generate_random_integer(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

def calculate_result(n1, n2, operator):
    """
    Calculate the result of the arithmetic operation specified by the operator.
    """
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    else:
        return n1 * n2

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(n1, n2, operator)
        print(f"\nQuestion: {n1} {operator} {n2}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
