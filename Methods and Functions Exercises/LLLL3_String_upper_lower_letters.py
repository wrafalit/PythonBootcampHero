# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!


def up_low(s):
    n_up = 0
    n_lo = 0
    for ch in s:
        if ch.isupper():
            n_up += 1
        elif ch.islower():
            n_lo += 1
    print('No. of Upper case characters : ', n_up)
    print('No. of Lower case Characters : ', n_lo)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))



