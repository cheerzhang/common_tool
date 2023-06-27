import streamlit as st
import random

def run_game():
    st.title("Number Guessing Game")
    st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number
    target_number = random.randint(1, 100)

    # Initialize the number of guesses
    num_guesses = 0

    while True:
        # Get user input
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

        # Increase the number of guesses
        num_guesses += 1

        # Compare the guess with the target number
        if guess < target_number:
            st.write("Too low! Guess higher.")
        elif guess > target_number:
            st.write("Too high! Guess lower.")
        else:
            st.write(f"Congratulations! You guessed the number {target_number} correctly in {num_guesses} attempts.")
            break

if __name__ == '__main__':
    run_game()
