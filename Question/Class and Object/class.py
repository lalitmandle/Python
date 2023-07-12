# A class to handle deposits and withdrawals from a bank 

import sys 
class Bank(object):
    """Bank related transactions""" 
    # to intialize name and balance instance variables
    def __init__(self,name, balance = 0.0):
        self.name = name
        self.balance = balance

    #to add deposit amount to existionf valance 
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("low Balance, can't withdraw the given amount")
        else:
            self.balance -= amount
        return self.balance
#using the Bank class 
#create an account with the given name and balance 0.00
name = input("Enter name: ")
b = Bank(name)

#repeat continuously till choice is 'e' or 'E
while(True):
    print('d-Deposit, w - withdwar, e -Exit')
    choice = input("Your choice: ")
    if choice == 'e'or choice == 'E':
        sys.exit()
    #amount for deposit or withdraw 
    amt = float(input('Enter amount: '))

    #do the transaction
        
    if choice == 'd' or choice == 'D':
        print("Balance after deposite: ", b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print("Balance after withdrawal: ", b.withdraw(amt))
