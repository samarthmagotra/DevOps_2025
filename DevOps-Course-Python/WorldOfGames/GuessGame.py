from abc import ABC, abstractmethod
import random

# Abstract base class
class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    @abstractmethod
    def generate_number(self):
        """Abstract method to generate a secret number."""
        pass

    @abstractmethod
    def get_guess_from_user(self):
        """Abstract method to get a guess from the user."""
        pass

    @abstractmethod
    def compare_results(self, user_guess):
        """Abstract method to compare the user's guess with the secret number."""
        pass

    @abstractmethod
    def play(self):
        """Abstract method to manage the game flow."""
        pass

# Concrete implementation of the Guess Game
class GuessGame(Game):
    def generate_number(self):
        """Generates a random number between 1 and the difficulty level."""
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        """Prompts the user for a guess and ensures it's within the valid range."""
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Invalid input! Enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def compare_results(self, user_guess):
        """Compares the user's guess with the secret number."""
        return user_guess == self.secret_number

    def play(self):
        """Plays the game by calling the appropriate methods."""
        print(f"Starting Guess Game with difficulty level: {self.difficulty}.")
        self.generate_number()
        print("A secret number has been generated.")
        user_guess = self.get_guess_from_user()
        if self.compare_results(user_guess):
            print(f"Congratulations! You guessed correctly. The secret number was {self.secret_number}.")
            return True
        else:
            print(f"Sorry, that's incorrect. The secret number was {self.secret_number}.")
            return False

# Example usage
if __name__ == "__main__":
    difficulty_level = 5  # You can set the difficulty level here
    game = GuessGame(difficulty_level)
    game.play()
