import random


def generate_number(n):
    return random.randint(1, n)


def get_guess_from_user(n):
    while True:
        try:
            num = int(input(f"This is a guessing game. Please choose a number between 1 - {n}: \n"))  # Verify input is int
            if not 1 < num < n:  # verify input is between 1 - difficulty
                print(f"Invalid Option, please choose a number between 1 - {n}: \n")
                continue
            else:
                return num
        except ValueError:
            print(f"Invalid Option, please enter a number between 1 - {n}: \n")
            continue


def compare_results(num1, num2):
    result = num1 == num2
    if result:
        print("You won!")
    else:
        print("You lost, try harder next time...")
    return result


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    compare_results(user_number, secret_number)





