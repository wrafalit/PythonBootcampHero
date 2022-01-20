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

display_board(test_board)
place_marker(test_board,'$',8)
display_board(test_board)
