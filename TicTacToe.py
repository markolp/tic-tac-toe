print("Welcome to Tic Tac Toe!")

from IPython.display import clear_output

# Step 1. Write a function that can print out a board. Set up your board as a list,
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board():
    # Create a function called "chunks" with two arguments, l and n:
    def chunks(l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i : i + n]

    # Create a list that from the results of the function chunks:
    new_board = list(chunks(board, 3))
    print("\n---------")
    for row in new_board:
        print(str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]))
        #         if row == [7,8,9]:
        #             break
        print("---------")


# Step 2. Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker_choice = input("Hello! Do you want to play as X or O? ").upper()

    while not (marker_choice == "X" or marker_choice == "O"):
        marker_choice = input("Sorry, you can choose only from X or O! ").upper()
    print("Good, you play as " + marker_choice + ".")
    return marker_choice

    if marker_choice == "X":
        print("You oppenent plays as O.")

    else:
        print("You oppenent plays as X.")


# Step 5. Write a function that uses a random module to randomly decide which player goes first.
# Return a string of which player went first.
import random


def choose_first():
    first_player = random.randint(1, 2)
    if first_player == 1:
        first_player = "X"
    else:
        first_player = "O"
    #     print('Player ' + str(first_player) + ' goes first!')
    return first_player


# Step 3. Write a function that takes, in the board list object, a marker ('X' or 'O'), and a desired position
# (number 1-9) and assigns it to the board.
def place_marker(current_player):
    display_board()
    position = 0

    # check if the position doesn't meet the requirements
    while True:
        show_palyer(current_player)
        # check if the position not in the range 1 to 9
        while not (position >= 1 and position <= 9):
            try:
                position = int(
                    input(
                        "Choose the location of your symbol? You can only choose from 1 to 9. "
                    )
                )
            except ValueError:
                print("Sorry, you can only choose from numbers 1 to 9.")

        # check if the position is equal to 'X'
        while not board[position - 1] != "X":
            try:
                print("This place is already occupied, choose another number.")
                position = int(
                    input(
                        "Choose the location of your symbol? You can only choose from 1 to 9. "
                    )
                )
            except ValueError:
                print("Sorry, you can only choose from numbers 1 to 9.")
        else:
            break
    board[position - 1] = current_player


# show which player turn
def show_palyer(current_player):
    if current_player == "X":
        print("\nNow the X player turn! ")
    else:
        print("\nNow the O player turn! ")


# check if the board has empty space
def full_board_check(board):
    for i in board:
        if type(i) == int:
            return False
    return True


# win checking
def win_check(board, mark):
    # row checking
    for i in range(0, 3):
        # row and col
        if (
            board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == mark
            or board[i] == board[i + 3] == board[i + 6] == mark
        ):
            return True
    if board[2] == board[4] == board[6] == mark:
        return True
    if board[0] == board[4] == board[8] == mark:
        return True
    return False


# Step 9. Write a function that asks the player if they want to play again and returns a boolean True
# if they do want to play again.
def replay():
    return (
        input(
            "That was an amazing gameplay! Would you like to play again? (Yes or No) "
        )
        .lower()
        .startswith("y")
    )


# game logic starts from here:
while True:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_input()
    current_player = choose_first()

    while not full_board_check(board):
        place_marker(current_player)
        if win_check(board, current_player):
            display_board()
            print("\nPlayer " + current_player + " Won! Congratulations!")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        clear_output()

    if not replay():
        break
