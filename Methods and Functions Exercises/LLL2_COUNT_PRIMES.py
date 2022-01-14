# COUNT PRIMES: Write a function that returns the number of prime numbers 
# that exist up to and including a given number

# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(num):
    count = 0
    i = 0
    list_primes = list(range(2,num))
    for n in list(range(2,num)):
        #print(n) check variable
        for nn in list(range(2,n+1)):
            #print('nn ',nn) check variable
            if n % nn == 0:
                i +=1
        #print('i ',i) check variable
        if i == 1:
            count += 1
        i = 0
    return count



# Check
print(count_primes(100))
