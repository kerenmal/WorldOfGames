import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG)",
          "Here you can find many cool games to play.", sep="\n")


def load_game():
    print("Please choose a game to play:",
            "   1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
            "   2. Guess Game - guess a number and see if you chose like the computer",
            "   3. Currency Roulette - try and guess the value of a random amount of USD in ILS", sep="\n")
    game_number = input("Game number: ")
    while game_number not in ['1','2','3']:
        game_number = input("please choose between 1-3: ")
    game_difficulty = input("Please choose game difficulty from 1 to 5: ")
    while game_difficulty not in ['1','2','3','4','5']:
        game_difficulty = input("please choose between 1-5: ")
    if game_number == "2":
        if GuessGame.play(game_difficulty):
            print("You won!")
            Score.add_score(game_difficulty)
        else:
            print("You lost!")
    elif game_number == "1":
        if MemoryGame.play(game_difficulty):
            print("You won!")
            Score.add_score(game_difficulty)
        else:
            print("You lost!")
    elif game_number == "3":
        if CurrencyRouletteGame.play(game_difficulty):
            print("You won!")
            Score.add_score(game_difficulty)
        else:
            print("You lost!")

