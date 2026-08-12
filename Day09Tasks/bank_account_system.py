# Q4 : Bank Account System (Class, Object, Constructor) A bank wants to manage customer accounts. Create a BankAccount class with a constructor to initialize account number and balance. Implement methods to deposit, withdraw, and display balance. 
class BankAccount:
    def __init__(self,accountnumber,balance):
        self.accountnumber = accountnumber
        self.balance = balance
    def deposit(self,amount):
            self.balance = self.balance + amount
            print("Deposited Amount :",amount)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn Amount:",amount)
        else:
            print("Insufficient Balance")
    def display_balance(self):
        print(self.accountnumber,self.balance)
acc = BankAccount("UBINO56789",50000)
acc.deposit(1000)
acc.withdraw(1500)
acc.display_balance()