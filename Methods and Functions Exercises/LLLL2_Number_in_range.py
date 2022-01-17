# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if low <= num <= high:
        print(f'{num} is in the range between {low} and {high}' )
    else:
        print(f'{num} is not in the range between {low} and {high}' )


# Check
# 5 is in the range between 2 and 7
print(ran_check(5,2,7))

#If you only wanted to return a boolean:


def ran_bool(num,low,high):
    return low <= num <= high

print(ran_bool(3,1,10))
