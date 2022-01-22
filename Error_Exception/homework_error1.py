# Exercise_1
print('# Exercise_1')
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('TypeError')

# Exercise_2
print('\n # Exercise_2')
try:
    x = 5
    y = 0

    z = x / y
except:
    print('ZeroDivisionError')
finally:
    print('Well Done!')

# Exercise_3
print('\n # Exercise_3')
def ask():
    while True:
        try:
            a = int(input('Input an integer: '))
        except:
            print("An error occurred! Please try again!" )
            continue
        else:
            print('Thank you, your number squared is: ', a ** 2)
            break



ask()