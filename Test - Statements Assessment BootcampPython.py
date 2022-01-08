# 1 Use for, .split(), and if to create a Statement that will print out words that start with 's':
from typing import List

st = 'Print only the words that start with s in this sentence'
temp = st.split()
sst: list[str] = []

for word in temp:
     if word[0] == 's':
         sst.append(word)

print(sst)

# 2 Use range() to print all the even numbers from 0 to 10.
mylist = [x for x in range(0,10) if x%2!=0]
print(mylist)

# 3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist2 = [x for x in range(0,50) if x%3==0]
print(mylist2)

# 4 Go through the string below and if the length of a word is even print "even!"
st1 = 'Print every word in this sentence that has an even number of letters'
temp =st1.split()
eword = []

for ch in temp:
    if len(ch)% 2 == 0:
        print(ch)

# 5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')

# 6 Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

print(x[0] for x in st.split())