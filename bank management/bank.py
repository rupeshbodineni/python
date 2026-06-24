
class bankmanagement():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited successfully")
    def withdraw(self,amount):
        if amount<0:
            print("invalid amount")
        elif amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"{amount} withdrawn successfully")
    def check_balance(self):   
        print(f"account holder:{self.name}")    
        print(f"account balance:{self.balance}") 

user=bankmanagement("rupesh",5000)
user.deposit(2000)
user.check_balance()
user.withdraw(1000)

user.check_balance()