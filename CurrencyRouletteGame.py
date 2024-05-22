import requests
import random


def get_money_interval(difficulty):
    base_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(base_url)
    data = response.json()
    exchange_rates = data["rates"]
    ILSrate=exchange_rates["ILS"]
    rand = random.randint(1, 100)
    total_amount = ILSrate * rand
    money_interval = (total_amount - (5 - int(difficulty)), total_amount + (5 - int(difficulty)))
    return rand, money_interval, total_amount


def get_guess_from_user(random):
    guess = input(f"what is {random} dollars in ILS:")
    return guess

def play(game_difficulty):
    values = get_money_interval(game_difficulty)
    guess = get_guess_from_user(values[0])
    print("The value is", values[2])
    return values[1][0] <= int(guess) <= values[1][1]

