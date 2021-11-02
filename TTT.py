'''
Andres Yengle
9-23
This is tic tac toe
'''

import random
#This is the board 2d-array

board = [["_","_","_"],["_","_","_"],["_","_","_"]]
win_x = [["X","X","X"],["X","X","X"],["X","X","X"]]
win_O = [["O","O","O"],["O","O","O"],["O","O","O"]]
def my_board():
    print("Cols    0    1    2")
    print("row-0",board[0])
    print("row-1",board[1])
    print("row-2",board[2])

print("Welcome to my game!" )

# do error handling
#This code sets values


def player_choosing():
    global player_choice
    global computer_choice
    player_choice = input("Please enter capital X or O")
    if (player_choice != "X") and (player_choice != "O"):
        print("LEARN YOUR LETTERS")
        player_choosing()
    if player_choice == "X":
        computer_choice = "O"
        print("The computer is ", computer_choice)
    if player_choice == "O":
        computer_choice = "X"
        print("The computer is ", computer_choice)

player_choosing()


def computer_move():
    comp_choice_row = random.randint(0,2)
    comp_choice_col = random.randint(0,2)
    if board[comp_choice_row][comp_choice_col] == "_":
        board[comp_choice_row][comp_choice_col] = computer_choice
        print("This is the computers move.")
        my_board()
    else:
        print("Please pick an empty space")
        computer_move()

def player_move():
    player_choice_row = input("What row would you like?")
    player_choice_col = input("What col would you like?")
    int_player_choice_row = int(player_choice_row)
    int_player_choice_col = int(player_choice_col)
    if board[int_player_choice_row][int_player_choice_col] == "_":
        board[int_player_choice_row][int_player_choice_col] = player_choice
        my_board()
    else:
        print("Please pick an empty space")
        player_move()

def play_game():
    while True:
        computer_move()
        if win_x[0] == board[0]:
            print("X Wins")
            break
        if win_x[1] == board[1]:
            print("X Wins")
            break
        if win_x[2] == board[2]:
            print("X Wins")
            break
        if win_O[0] == board[0]:
            print("O Wins")
            break
        if win_O[1] == board[1]:
            print("O Wins")
            break
        if win_O[2] == board[2]:
            print("O Wins")
            break
        if(((board[0][0] == "X") and board[1][0] == "X") and board[2][0] == "X"):
            print("X Wins")
            break
        if (((board[0][1] == "X") and board[1][1] == "X") and board[2][1] == "X"):
            print("X Wins")
            break
        if (((board[0][2] == "X") and board[1][2] == "X") and board[2][2] == "X"):
            print("X Wins")
            break
        if (((board[0][0] == "O") and board[1][0] == "O") and board[2][0] == "O"):
            print("O Wins")
            break
        if (((board[0][1] == "O") and board[1][1] == "O") and board[2][1] == "O"):
            print("O Wins")
            break
        if (((board[0][2] == "O") and board[1][2] == "O") and board[2][2] == "O"):
            print("O Wins")
            break
            #Diagnols
        if (((board[0][0] == "X") and board[1][1] == "X") and board[2][2] == "X"):
            print("X Wins")
            break
        if (((board[0][2] == "X") and board[1][1] == "X") and board[2][0] == "X"):
            print("X Wins")
            break
        if (((board[0][0] == "O") and board[1][1] == "O") and board[2][2] == "O"):
            print("O Wins")
            break
        if (((board[0][2] == "O") and board[1][1] == "O") and board[2][0] == "O"):
            print("O Wins")
            break
        player_move()
        if win_x[0] == board[0]:
            print("X Wins")
            break
        if win_x[1] == board[1]:
            print("X Wins")
            break
        if win_x[2] == board[2]:
            print("X Wins")
            break
        if win_O[0] == board[0]:
            print("O Wins")
            break
        if win_O[1] == board[1]:
            print("O Wins")
            break
        if win_O[2] == board[2]:
            print("O Wins")
            break
        if(((board[0][0] == "X") and board[1][0] == "X") and board[2][0] == "X"):
            print("X Wins")
            break
        if (((board[0][1] == "X") and board[1][1] == "X") and board[2][1] == "X"):
            print("X Wins")
            break
        if (((board[0][2] == "X") and board[1][2] == "X") and board[2][2] == "X"):
            print("X Wins")
            break
        if (((board[0][0] == "O") and board[1][0] == "O") and board[2][0] == "O"):
            print("O Wins")
            break
        if (((board[0][1] == "O") and board[1][1] == "O") and board[2][1] == "O"):
            print("O Wins")
            break
        if (((board[0][2] == "O") and board[1][2] == "O") and board[2][2] == "O"):
            print("O Wins")
            break
        if (((board[0][0] == "X") and board[1][1] == "X") and board[2][2] == "X"):
            print("X Wins")
            break
        if (((board[0][2] == "X") and board[1][1] == "X") and board[2][0] == "X"):
            print("X Wins")
            break
        if (((board[0][0] == "O") and board[1][1] == "O") and board[2][2] == "O"):
            print("O Wins")
            break
        if (((board[0][2] == "O") and board[1][1] == "O") and board[2][0] == "O"):
            print("O Wins")
            break



play_game()











