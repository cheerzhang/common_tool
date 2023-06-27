import streamlit as st

# Initialize the Tic-Tac-Toe board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Define the player markers
player1_marker = 'X'
player2_marker = 'O'

# Define the current player
current_player = player1_marker

# Main game logic
def main():
    st.title("Tic-Tac-Toe")
    st.write("Player 1: X")
    st.write("Player 2: O")
    st.write("Let's play!")

    # Display the Tic-Tac-Toe board
    for row in board:
        st.write(row)

    # Let the players make their moves
    while True:
        row = st.number_input("Enter the row (0, 1, or 2):", min_value=0, max_value=2, step=1)
        column = st.number_input("Enter the column (0, 1, or 2):", min_value=0, max_value=2, step=1)

        # Check if the selected position is valid
        if board[row][column] != '':
            st.warning("Invalid move. Please select an empty position.")
            continue

        # Make the move
        board[row][column] = current_player

        # Check if the current player has won
        if check_winner(current_player):
            st.write(f"Player {current_player} wins!")
            break

        # Check if it's a draw
        if check_draw():
            st.write("It's a draw!")
            break

        # Switch to the next player
        current_player = player2_marker if current_player == player1_marker else player1_marker

# Function to check if a player has won
def check_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if it's a draw
def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

# Run the game
if __name__ == "__main__":
    main()
