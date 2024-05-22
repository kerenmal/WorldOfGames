import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return str(secret_number)


def get_guess_from_user(difficulty):
    guess = input(f"please choose between 1 to {difficulty}:")
    return guess


def compare_results(secret, guess):
    if secret == guess:
        return True
    else:
        return False


def play(game_difficulty):
    secret = generate_number(game_difficulty)
    guess = get_guess_from_user(game_difficulty)
    return compare_results(secret, guess)

