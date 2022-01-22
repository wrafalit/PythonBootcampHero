
def user_choice():
    x = ''
    while x.isdigit() == False:
        x = input('please enter a number: ')
        if x.isdigit() == False:
            print('\n'*100)
            print('Sorry its not a number!')
    return int(x)

user_choice()
