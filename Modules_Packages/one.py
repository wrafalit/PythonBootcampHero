#one.py

def func():
    print('Func() in one.py')

print('Top Level in one.py')

if __name__ == '__main__':
    print('ONE.py is being run directly')
else:
    print('One.py has been imported')