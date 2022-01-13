
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    doll_text = ''
    for ch in text:
        doll_text= doll_text + ch*3
    return doll_text
    
print(paper_doll('Hello'))
print(paper_doll('Mississippi')) 
