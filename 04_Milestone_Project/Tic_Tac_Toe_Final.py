import random

def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('- '+' '+' - '+" "+" - ")
    print(f'{board[2]} | {board[3]} | {board[4]}')

def choose_first():
    first = random.randint(1,2)
    return print('Start player ',first)
    
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
    return p_input
    
def place_marker(board, marker, position):
    board[position] =marker
    return board

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
    return p_choice

def space_check(board, position):
    if not board[position] == ' ':
        return False
    else:
        return True

    
test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]    
print('Welcome to Tic Tac Toe!')

while True:
    display_board(test_board)
    game_on = True
    choose_first()
    player_input()
    while game_on:
        player_choice(test_board)
        space_check(test_board,p_choice)
        place_marker(test_board, p_input, p_choice)
        #display_board(test_board)
        
        # Player2's turn.
            
            #pass

    #if not replay():
       # #break
