import streamlit as st
import random

# Define the possible moves
moves = ["Rock", "Paper", "Scissors"]

# Define the game logic
def play_game(player_move):
    # Generate a random move for the computer
    computer_move = random.choice(moves)

    # Determine the winner
    if player_move == computer_move:
        result = "It's a tie!"
    elif (
        (player_move == "Rock" and computer_move == "Scissors")
        or (player_move == "Paper" and computer_move == "Rock")
        or (player_move == "Scissors" and computer_move == "Paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    # Display the game result
    st.write(f"You chose: {player_move}")
    st.write(f"Computer chose: {computer_move}")
    st.write(result)


# Main page content
st.markdown("# Game - Rock, Paper, Scissors ❄️")
st.write("Welcome to the Rock, Paper, Scissors game!")
st.sidebar.markdown("# Rock, Paper, Scissors game ❄️")

# Main game logic
def main():
    st.title("Rock, Paper, Scissors")
    st.write("Make your move:")

    # Let the player select their move
    player_move = st.radio("Select your move", moves)

    # Play the game when the player clicks the "Play" button
    if st.button("Play"):
        play_game(player_move)

# Run the game
if __name__ == "__main__":
    main()

