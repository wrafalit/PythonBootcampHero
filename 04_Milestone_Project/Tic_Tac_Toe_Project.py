# Tic Tac Toe game.

# Here are the requirements:
#     2 players should be able to play the game (both sitting at the same computer)
#     The board should be printed out every time a player makes a move
#     You should be able to accept input of the player position and then place a symbol on the board

def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{board[2]} | {board[3]} | {board[4]}')

def player_input():
    p_input = ''
    while p_input.lower() not in ['x','o']:
        p_input = input('Please choose X or O: ')
        if p_input.lower() not in ['x','o']:
            print('\n'*100)
            print('Wrong letter')
            print('Please choose X or O ')
        else:
            pass
def place_marker(board, marker, position):
    board[position] =marker
    return board

def win_check(board, mark):
    win = False
    if board[1] == mark and board[2] == mark and board[3] == mark:
        win = True
        return print(win)
    if board[4] == mark and board[5] == mark and board[6] == mark:
        win = True
        return print(win)
    if board[7] == mark and board[8] == mark and board[9] == mark:
        win = True
        return print(win)
    if board[1] == mark and board[4] == mark and board[7] == mark:
        win = True
        return print(win)
    if board[2] == mark and board[5] == mark and board[8] == mark:
        win = True
        return print(win)
    if board[3] == mark and board[6] == mark and board[9] == mark:
        win = True
        return print(win)
    if board[1] == mark and board[5] == mark and board[9] == mark:
        win = True
        return print(win)
    if board[3] == mark and board[5] == mark and board[7] == mark:
        win = True
        return print(win)
    else:
        win = False
        return print(win)

import random

def choose_first():
    first = random.randint(1,2)
    return print(first)
    

display_board(test_board)
place_marker(test_board,'X',8)
display_board(test_board)
win_check(test_board,'X')
choose_first()
