# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    multiply = 0
    for n in numbers:
        if multiply != 0:
            multiply = multiply*n
        else:
            multiply = n
    print(multiply)

multiply([1,2,3,-4])
