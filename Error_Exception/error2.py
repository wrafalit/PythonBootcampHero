try:
    f = open('testfile','w')
    f.write('Write a test line')
except:
    print('All other exception')
finally:
    print("I always run")