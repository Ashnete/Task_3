"""
Word Scramble Game

The player is presented with a scrambled word and must guess
the correct original word from a predefined list.
"""

import random


def scramble_word(word):
    """
    Scrambles the letters of a given word.

    Args:
        word (str): The original word.

    Returns:
        str: A scrambled version of the word.
    """
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)


def play_game():
    """
    Runs the main logic for the word scramble game.
    """
    word_list = ['python', 'javascript', 'java',
                 'automation', 'pytest', 'guvi', 'selenium']

    # Choose a random word from the list
    original_word = random.choice(word_list)
    scrambled = scramble_word(original_word)

    print("🔀 Welcome to the Word Scramble Game!")
    print("Unscramble the letters to guess the word.")
    print(f"Scrambled word: {scrambled}")

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = input("Your guess: ").strip().lower()
        attempts += 1

        # Check if the guess matches the original word
        if guess == original_word:
            print(f"✅ Correct! You guessed it in {attempts} attempt(s).")
            break
        else:
            print("❌ Incorrect guess.")
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Try again. Attempts left: {remaining}")
            else:
                print("🚫 Out of attempts. Game Over!")
                print(f"The correct word was: '{original_word}'")


if __name__ == "__main__":
    play_game()
