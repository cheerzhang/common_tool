import streamlit as st
import random

# Define the list of words for the game
words = ["apple", "banana", "orange", "watermelon", "strawberry", "grapefruit"]

# Select a random word from the list
word = random.choice(words)

# Initialize the game state
guessed_letters = []
num_attempts = 6

# Main game logic
def main():
    st.title("Hangman")
    st.write("Guess the word!")

    # Display the current game state
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    st.write(display_word)

    # Let the player enter a letter
    letter = st.text_input("Enter a letter").lower()

    # Validate the input
    if not letter.isalpha() or len(letter) != 1:
        st.warning("Please enter a single letter.")
        return

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        st.warning("You have already guessed that letter.")
        return

    # Update the game state
    guessed_letters.append(letter)

    # Check if the letter is in the word
    if letter in word:
        st.success("Correct guess!")
    else:
        st.error("Wrong guess!")
        num_attempts -= 1

    # Check if the game is over
    if num_attempts == 0:
        st.write("Game over! You lost.")
        st.write(f"The word was: {word}")
    elif all(letter in guessed_letters for letter in word):
        st.write("Congratulations! You won.")
    else:
        st.write(f"You have {num_attempts} attempts left.")

# Run the game
if __name__ == "__main__":
    main()
