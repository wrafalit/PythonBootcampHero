class Account:
    
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner: {self.owner}\n
    def deposit(self,money):
        self.balance = self.balance + money
        print('Deposit Accepted')
        
    def withdraw(self, money):
        if self.balance - money > 0:
            self.balance = self.balance - money
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
    
        
acct1 = Account('Jose',100)

print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.balance)
print(acct1.withdraw(775))
