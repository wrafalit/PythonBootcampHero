# Pig Latin
# If a word starts with a vowel, add 'ay' to end
# if a word does not start with a vowel, put first letter at the end, then add 'ay'
# word --> ordway
# apple --> appleay

def pig_latin(word):
    if word[0].upper() in ['A','E', 'I', 'O', 'U', 'Y']:
        return word[1:] + word[0] + 'ay'
    else:
        return word + 'ay'

print(pig_latin('apple'))
