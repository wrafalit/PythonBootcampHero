#two.py

import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
    print('Two is being run directly!')
else:
    print('Two.py has been imported')