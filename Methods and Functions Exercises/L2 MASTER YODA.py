# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'



def master_yoda(name):
    i = 0
    rev = []
    name_list = name.split()
    print('name_list' , name_list[1:2])
    i = len(name_list)
    if i > 0:
        rev += name_list[2]
        print('i' , i)
        print('rev: ', rev)
        return rev
        
print(master_yoda('I am home'))

