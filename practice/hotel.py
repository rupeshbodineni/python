class bankaccount:
    def __init__(self,name,accountno,balance=0):
        self.name=name
        self.accountno=accountno
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            print(f"{amount} deposited successfully")