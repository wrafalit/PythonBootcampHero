def ask_for_int():
    result = ''
    while type(result) != int:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops that is not a number')
        finally:
            print('End of try/except/finaly')

ask_for_int()