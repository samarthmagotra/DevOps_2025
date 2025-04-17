from abc import ABC, abstractmethod
import random
import time
import os

# Abstract base class
class Game(ABC):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    @abstractmethod
    def generate_sequence(self):
        """Abstract method to generate a sequence of numbers."""
        pass

    @abstractmethod
    def get_list_from_user(self):
        """Abstract method to prompt the user for a list of numbers."""
        pass

    @abstractmethod
    def is_list_equal(self, generated_sequence, user_sequence):
        """Abstract method to compare two lists."""
        pass

    @abstractmethod
    def play(self):
        """Abstract method to handle the game's flow."""
        pass


# Concrete class implementing the Memory Game
class MemoryGame(Game):
    def generate_sequence(self):
        """Generates a list of random numbers with a length equal to the difficulty."""
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        """Prompts the user to input a sequence of numbers."""
        print(f"Please enter {self.difficulty} numbers that you remember:")
        user_sequence = []
        for i in range(self.difficulty):
            while True:
                try:
                    num = int(input(f"Number {i + 1}: "))
                    user_sequence.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        return user_sequence

    def is_list_equal(self, generated_sequence, user_sequence):
        """Compares the generated sequence with the user's input."""
        return generated_sequence == user_sequence

    def play(self):
        """Main game logic that combines all methods."""
        print(f"Welcome to the Memory Game! Difficulty level: {self.difficulty}")

        # Generate a random sequence
        generated_sequence = self.generate_sequence()
        print(f"Remember this sequence: {generated_sequence}")

        # Display the sequence for 0.7 seconds
        time.sleep(0.7)
        print("\033c", end="")  # Clears the screen (Linux/Mac).
        #os.system('cls' if os.name == 'nt' else 'clear')

        # Get the user input
        user_sequence = self.get_list_from_user()

        # Check if the user's list matches the generated sequence
        if self.is_list_equal(generated_sequence, user_sequence):
            print("Congratulations! You remembered all the numbers correctly. You win!")
            return True
        else:
            print(f"Sorry, you were incorrect. The correct sequence was: {generated_sequence}")
            return False


if __name__ == "__main__":
    difficulty_level = 5  # You can modify the difficulty level as needed
    game = MemoryGame(difficulty_level)
    game.play()
