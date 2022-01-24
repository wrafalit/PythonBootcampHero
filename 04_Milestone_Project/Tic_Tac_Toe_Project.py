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

def space_check(board, position):
    if not board[position] == ' ':
        return False
    else:
        return True

    def full_board_check(board):
    count = 0
    for i in range(1,len(board)):
        if board[i] == ' ':
            count += 1
    if count > 0:
        return True
    else:
        return False

  
def player_choice(board):
    p_choice = ''
    w_range = False
    while p_choice.isdigit() == False or w_range == False:
        p_choice = input('Choose number 1-9: ')
        
        if p_choice.isdigit() == False:
            print('Wrong number')
        if p_choice.isdigit() == True:
            if int(p_choice) in range(1,10):
                w_range = True
            else:
                w_range = False
    print(space_check(test_board, int(p_choice)))

def replay():
    p_rep = ''
    while p_rep.lower not in ['y','n']:
        p_rep= input('If you want to play again?. press Y-yes, N-no: ')
        if p_rep == 'y':
            return True
        elif p_rep == 'n':
            return False
    
display_board(test_board)
place_marker(test_board,'X',8)
display_board(test_board)
win_check(test_board,'X')
choose_first()
space_check(test_board,4)
full_board_check(test_board)
player_choice(test_board))
replay()
