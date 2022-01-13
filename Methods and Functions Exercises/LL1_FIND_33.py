# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(num_list):
    i = 0
    while i < (len(num_list) -1):
        if num_list[i] == 3 and num_list[i] == num_list[i+1]:
            return True
        i += 1
    else:
        return False

        
            
            
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([1, 3, 1, 3, 5, 3, 3]))
