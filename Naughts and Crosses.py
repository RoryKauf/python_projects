from random import randint

def display_board(board):
    print(f"   |   |   \n {board[1]} | {board[2]} | {board[3]} \n___|___|___\n   |   |   \n {board[4]} | {board[5]} | {board[6]} \n___|___|___\n   |   |  \n {board[7]} | {board[8]} | {board[9]} \n   |   |   ")

def player_input():
    while True:
        try:
            player_input = input("Please select X or O\n")
            if player_input.upper() == "X":
                return ("X","O")
            elif player_input.upper() == "O":
                return ("O","X")
        except:
            print("Please only select X or O")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (board[1] == marker and board[2] == marker and board[3] == marker) or \
           (board[4] == marker and board[5] == marker and board[6] == marker) or \
           (board[7] == marker and board[8] == marker and board[9] == marker) or \
           (board[1] == marker and board[4] == marker and board[7] == marker) or \
           (board[2] == marker and board[5] == marker and board[8] == marker) or \
           (board[3] == marker and board[6] == marker and board[9] == marker) or \
           (board[1] == marker and board[5] == marker and board[9] == marker) or \
           (board[3] == marker and board[5] == marker and board[7] == marker)

def randomise():
    choice = randint(1,2)
    if choice == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for space in board:
        if space == " ":
            return False
    return True

def player_choice(board):
    while True:
        player_input = input("Please pick your square, 1 - 9\n")
        if int(player_input) in range(1,10):
            if space_check(board, int(player_input)) == True:
                return int(player_input)
            else:
                print("Sorry your number is taken, please select another one")
        else:
            print("Please only select a number 1 through to 9")

def replay():
    while True:
        replay = input("Would you like to play another game? Y/N?\n")
        if replay.upper() == "Y" or replay.upper() == "N":
            if replay.upper() == "Y":
                return True
            else:
                return False
        else:
            print("Please only select Y or N\n")

def comp_move(board):
    while True:
        comp_num = randint(1,9)
        if int(comp_num) in range(1, 10):
            if space_check(board, comp_num) == True:
                return comp_num

def player_turn(x_or_o, turn):
    marker = x_or_o[turn]
    if marker == x_or_o[0]:
        print(f"\nIt's your's turn.")
        place_marker(board, marker, player_choice(board))
        print("Your board looks like:")
        display_board(board)
        if win_check(board,marker):
            print(f"Congratulations, you've won")
            switch = 1
            return switch
        elif full_board_check(board):
            print("There's no spaces left, it's a draw")
            switch = 1
            return switch
    else:
        comp_turn = comp_move(board)
        print(f"\nIt's the computer's turn. They've chosen square {comp_turn}")
        place_marker(board, marker, comp_turn)
        display_board(board)
        if win_check(board, marker):
            print(f"The computwr has won")
            switch = 1
            return switch
        elif full_board_check(board):
            print("There's no spaces left, it's a draw")
            switch = 1
            return switch

while True:
    board = ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print('\nEach turn you will be asked to select a square as per the board below. First to get three in a row wins.\n')
    print(f"   |   |   \n 1 | 2 | 3 \n___|___|___\n   |   |   \n 4 | 5 | 6 \n___|___|___\n   |   |  \n 7 | 8 | 9 \n   |   |   \n")
    x_or_o = player_input()
    if randomise() == "Player 1":
        p1_turn = 0
        p2_turn = 1
    else:
        p1_turn = 1
        p2_turn = 0
    print(f"{x_or_o[p1_turn]} goes first")
    switch = 0
    while switch != 1:
        switch = player_turn(x_or_o, p1_turn)
        if switch == 1:
            break
        switch = player_turn(x_or_o, p2_turn)
        if switch == 1:
            break
    if not replay():
        break
