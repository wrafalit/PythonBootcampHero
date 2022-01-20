# Tic Tac Toe game.

# Here are the requirements:
#     2 players should be able to play the game (both sitting at the same computer)
#     The board should be printed out every time a player makes a move
#     You should be able to accept input of the player position and then place a symbol on the board

def display_board(b):
    print(f'{b[7]} | {b[8]} | {b[9]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{b[4]} | {b[5]} | {b[6]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{b[2]} | {b[3]} | {b[4]}')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
