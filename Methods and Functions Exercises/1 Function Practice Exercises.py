# LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(num1,num2):
    if num1 % 2 == 0 and num2 % 2 ==0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 < num2:
            return num2
        else:
            return num1
# Check 1
print(lesser_of_two_evens(2,4))
# Check 2
print(lesser_of_two_evens(2,5))