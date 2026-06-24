
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

name=input("enter yout name:")
balance=float(input("enter opening bonus:"))
account=bankmanagement(name,balance)
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.checkbalance")
    print("4.exit")

    choice=int(input("select an option:"))
    if choice==1:
        amount=float(input("enter the amount:"))
        account.deposit(amount)

    elif choice==2:
        amount=int(input("enter the withdrawn amount:"))
        account.withdraw(amount)

    elif choice==3:
        account.check_balance()

    elif choice==4:
        print("thank you for using bank management system")
        break
    else:
        print("invalid choice")