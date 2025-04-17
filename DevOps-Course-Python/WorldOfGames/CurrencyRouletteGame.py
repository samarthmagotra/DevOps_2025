import json
import random
import requests
from abc import ABC, abstractmethod


# Abstract base class
class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @abstractmethod
    def get_money_interval(self):
        """Abstract method to calculate the interval."""
        pass

    @abstractmethod
    def get_guess_from_user(self):
        """Abstract method to get the user's guess."""
        pass

    @abstractmethod
    def play(self):
        """Abstract method to handle game play."""
        pass


# Concrete class for Currency Roulette Game
class CurrencyRouletteGame(Game):
    def get_money_interval(self):
        """Fetch the currency rate from USD to ILS and generate the interval."""
        # Replace with the actual API URL if available; here, we simulate the exchange rate.
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            exchange_rate = response.json()["rates"]["ILS"]
            print(response.json())
            print(json.dumps(response.json(),indent=4))
        except:
            # Fallback rate in case of API failure
            exchange_rate = 3.5  # Example exchange rate

        total_value = random.randint(1, 100)
        print(f"The USD amount is: {total_value}")

        # Calculate the interval based on difficulty
        interval_margin = 5 - self.difficulty
        lower_bound = total_value * exchange_rate - interval_margin
        upper_bound = total_value * exchange_rate + interval_margin

        return lower_bound, upper_bound, total_value

    def get_guess_from_user(self):
        """Prompt the user for a guess."""
        while True:
            try:
                user_guess = float(input("Enter your guess for the amount in ILS: "))
                return user_guess
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def play(self):
        """Play the game."""
        print(f"Welcome to the Currency Roulette Game! Difficulty level: {self.difficulty}")

        # Generate the interval and get the exchange rate
        lower_bound, upper_bound, usd_value = self.get_money_interval()
        print(f"The interval is generated (hidden from user): ({lower_bound}, {upper_bound})")

        # Get the user's guess
        user_guess = self.get_guess_from_user()

        # Check if the user's guess falls within the interval
        if lower_bound <= user_guess <= upper_bound:
            print("Congratulations! Your guess was correct!")
            return True
        else:
            print(f"Sorry, your guess was incorrect. The correct interval was: ({lower_bound:.2f}, {upper_bound:.2f})")
            print(f"The value in ILS for {usd_value} USD is approximately {usd_value * 3.5:.2f}")
            return False


# Example usage
if __name__ == "__main__":
    difficulty_level = 3  # Adjust the difficulty level here
    game = CurrencyRouletteGame(difficulty_level)
    game.play()
