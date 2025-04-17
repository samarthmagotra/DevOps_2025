from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame

def welcome(name:str):
    return f'Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.'

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    # Get and validate the game choice
    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play (1-3): "))
            if game_choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Get and validate the difficulty level
    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"You chose Game {game_choice} with difficulty level {difficulty}.")

#Updated code for Function Update
    if game_choice == 1:
        game = MemoryGame(difficulty)
        game.play()
    elif game_choice == 2:
        game = GuessGame(difficulty)
        game.play()
    else:
        game = CurrencyRouletteGame(difficulty)
        game.play()






