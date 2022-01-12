# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(name):
    revi = []
    list_name = name.split()
    for word in list_name[::-1]:
        revi.append(word)
    return revi


print(master_yoda('I am home'))
