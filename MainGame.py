from Live import load_game, welcome
print(welcome("Keren"))
load_game()
endgame = input("Do you want to play again? yes/no: ")
while endgame != "no":
    load_game()
    endgame = input("Do you want to play again? yes/no: ")