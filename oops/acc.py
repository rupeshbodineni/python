class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno

    def debit(self,amount):
        self.balance=-amount
        print("rs",amount,"was debited")
        print("total balance=",self.balance)
    def credit(self,amount):
        self.balance=+amount
        print("rs",amount,"was credited")
        print("total balance=",self.balance)
    def balance(self):
        return self.balance
    
Account1=Account(1000,1234)
Account1.debit(1000)
Account1.credit(500)