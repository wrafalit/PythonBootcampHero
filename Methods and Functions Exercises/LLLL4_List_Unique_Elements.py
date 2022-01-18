# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    uniq_lst = {}
    uniq_num = []
    for n in range(len(lst)):
        if lst[n] in uniq_lst:
            uniq_lst[lst[n]] += 1
        else:
            uniq_lst[lst[n]] = 1
    for k,v in uniq_lst.items(): # no duplicate number (unique)
        if v == 1:
            uniq_num.append(k)
            
    print('Sample List : ', lst)
    print('Unique List : ',uniq_lst)
    print('no duplicate number (unique): ', uniq_num)
    
# def unique_list(lst):
#    unique = []
#    for n in lst:
#        if n not in unique:
#            unique.append(n)
#    print(unique)
  
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
