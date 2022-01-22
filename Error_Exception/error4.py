def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops that is not a number')
            continue
        else:
            print('Its a number')
            break
        finally:
            print('End of try/except/finaly')

ask_for_int()