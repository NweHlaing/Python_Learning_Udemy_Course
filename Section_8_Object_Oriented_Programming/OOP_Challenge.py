class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Nwe',100)
print("Account info",acct1)
print("Owner Name: ",acct1.owner)
print("Balance: ",acct1.balance)

acct1.deposit(100)
acct1.withdraw(200)