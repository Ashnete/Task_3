"""
Guess the Number Game

This game generates a random number between 1 and 100,
and the player has to guess it through multiple attempts.
"""

import random

def main():
    """Main function to run the guess the number game."""
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize guess to None and attempts to 0
    guess = None
    attempts = 0
    max_attempts = 10

    print(" Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Loop until the player guesses correctly
    while guess != secret_number:
        try:
            # Get user input and convert it to integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            elif attempts > max_attempts:
                # If the player exceeds the maximum number of allowed attempts, end the game
                print(f" You've exceeded the maximum number of attempts ({max_attempts}). Game over!")
            else:
                print(f" Correct! You guessed the number in {attempts} attempts.")

        except ValueError:
            print(" Please enter a valid integer.")

if __name__ == "__main__":
    main()
