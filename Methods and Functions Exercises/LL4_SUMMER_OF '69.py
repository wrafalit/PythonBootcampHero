
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    i = len(arr)
    n6 = 0
    n9 = 0
    summ = 0
    #print(i)
    for n in range(len(arr)):
        if arr[n] == 6:
            n6 = n
            #print(n6)
        if arr[n] == 9:
            n9 = n
            #print(n9)
    if n6 != 0 and n9 !=0:
        del arr[n6:n9+1]
        return sum(arr)
    else:
        return sum(arr)
    

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# example below is not working correct if are to slicers 6:9
# problem to fix 
print(summer_69([2, 1, 6, 9,11,2,4]))
