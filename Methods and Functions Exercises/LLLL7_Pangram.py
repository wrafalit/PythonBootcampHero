# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Hint: You may want to use .replace() method to get rid of spaces.

# Hint: Look at the string module

# Hint: In case you want to use set comparisons

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    parag = set((str1.lower()).replace(' ',''))
    print(parag.issuperset(set(alphabet)))
 
# Check_1   
ispangram("The quick brown fox jumps over the lazy dog")
# True

# Check_2
ispangram("The quick brown fox and lazy dog")
#False
