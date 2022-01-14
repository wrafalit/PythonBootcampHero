# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    add = True
    bond_list = []
    for n in nums:
        if n ==0:
            bond_list.append(n)
        elif n==7:
            bond_list.append(n)
    if bond_list == [0, 0, 7]:
        return True
    else:
        return False
            

# Check
print(spy_game([1,2,4,0,0,7,5]))

# Check
print(spy_game([1,0,2,4,0,5,7]))

# Check
print(spy_game([1,7,2,0,4,5,0]))

# Solution not working for list with more 0 or 7 than 007 number
print(spy_game([1,2,4,0,0,7,5,0,0]))
