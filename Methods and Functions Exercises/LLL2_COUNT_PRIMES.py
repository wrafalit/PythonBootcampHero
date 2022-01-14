# COUNT PRIMES: Write a function that returns the number of prime numbers 
# that exist up to and including a given number

# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(num):
    count = 0
    list_primes = list(range(2,num))
    for n in list(range(2,num)):
        if n % 1 == 0 and n % n == 0:
            count += 1
            
    print(list_primes)
    print(count)
    pass
                

# Check
print(count_primes(10))
