# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
# if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    #print(a)
    for num in (a,b,c):
        if 1<= num <= 11:
            if sum((a,b,c)) <= 21:
                return sum((a,b,c))
            elif sum((a,b,c)) > 21 and (a == 11 or b==11or c ==11):
                return (sum((a,b,c))-10)
            else:
                return 'BUST'
        else:
            print('integers must be between 1 and 11')

    
print(blackjack(5,6,7))  
print(blackjack(9,9,9))  
print(blackjack(9,9,11))  
