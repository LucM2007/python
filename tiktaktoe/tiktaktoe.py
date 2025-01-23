"""
this is to play a game of tic-tac-toe
"""
print("Welcome to tic-tac-toe!")
winner = "still going"
while True:
    play = input("do you want to play (yes/no)").capitalize()
    if play != "Yes" and play != "No": # checks input
        continue
    elif play == "No":
        break
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # makes the board
    goes_first = input("Who will go first? (X or O)").capitalize()
    if goes_first == 'X': #who goes first
        turn = "X"
    elif goes_first == 'O':
        turn = "O"
    else:
        print("Please enter a valid input")
        continue
    print(board[0], board[1], board[2]) #shows the board
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    while True:
        input_position = input("Enter a position (1-9): ")
        if not input_position.isdigit(): #check if input is a digit
            print("Please enter a valid number between 1 and 9")
            continue
        if int(input_position) > 9 or int(input_position) < 1: # if its between 1 and 9
            print("Please enter a valid number between 1 and 9")
            continue
        if board[int(input_position) - 1] == "X" or board[int(input_position) - 1] == "O": # checks if that position is available
            print(f'Position {input_position} is already taken')
            continue
        replace_position = input_position
        replace_position = int(replace_position)
        replace_position = board[replace_position - 1]

        if turn == "X": # switches what is placed on the board where the user chose and give the other player the turn
            board[replace_position - 1] = "X"
            turn = "O"
        elif turn == "O":
            board[replace_position - 1] = "O"
            turn = "X"
        print(board[0], board[1], board[2]) # shows board to user
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        if board[0] == board[1] == board[2] == "X":   # 1st row
            winner = "X"
        elif board[3] == board[4] == board[5] == "X": # 2nd row
            winner = "X"
        elif board[6] == board[7] == board[8] == "X": # 3rd row
            winner = "X"
        elif board[0] == board[3] == board[6] == "X": # 1st column
            winner = "X"
        elif board[1] == board[4] == board[7] == "X": # 2nd column
            winner = "X"
        elif board[2] == board[5] == board[8] == "X": # 3rd column
            winner = "X"
        elif board[0] == board[4] == board[8] == "X": # diagonal top left to bottom right
            winner = "X"
        elif board[2] == board[4] == board[6] == "X": # diagonal top right to bottom left
            winner = "X"
        elif board[0] == board[1] == board[2] == "O": # 1st row
            winner = "O"
        elif board[3] == board[4] == board[5] == "O": # 2nd row
            winner = "O"
        elif board[6] == board[7] == board[8] == "O": # 3rd row
            winner = "O"
        elif board[0] == board[3] == board[6] == "O": # 1st column
            winner = "O"
        elif board[1] == board[4] == board[7] == "O": # 2nd column
            winner = "O"
        elif board[2] == board[5] == board[8] == "0": # 3rd column
            winner = "O"
        elif board[0] == board[4] == board[8] == "0": # diagonal top left to bottom right
            winner = "O"
        elif board[2] == board[4] == board[6] == "O": # diagonal top right to bottom left
            winner = "O"
        elif board[0] == 1 or board[1] == 2 or board[2] == 3 or board[3] == 4 or board[4] == 5 or board[5] == 6 or board[6] == 7 or board[7] == 8 or board[8] == 9:
            continue # checks if there still is an open spot
        else:
            winner = "tie"
        if winner != "still going":
            if winner == "tie":
                print("It's a tie!")
            else:
                print(f'The winner is {winner}')
            winner = "still going"
            break