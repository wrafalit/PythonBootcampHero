# ANIMAL CRACKERS
# Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(strin):
    list_word = strin.split()
    if list_word[0][0] == list_word[1][0]:
        return True
    else:
        return False

# Check 1
print(animal_crackers('Levelheaded Llama'))
# Check 2
print(animal_crackers('Crazy Kangaroo'))