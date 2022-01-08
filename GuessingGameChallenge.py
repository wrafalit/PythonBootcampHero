import random
from random import randint

random = random.randint(1,100)
guesses = []

print('Guess number from 1 to 100:')
print(f'Number {random}')
while True:
    guess = int(input())
    guesses.append(guess)
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS"')
    elif random == guess:
            break
    else:
        if len(guesses) == 1:
            if abs(random - guess) <= 10:
                print('WARM')
            else:
                print('COLD')
        else:
            if abs(guesses[-1] - random) < abs(guesses[-2] - random):
                print('WARMER')
            else:
                print('COLDER')

print('WINER')
print(f'You guess number! It is {guess} and it took {len(guesses)} you guesses ')
#print(guesses)
