class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def  debit(self,amount):

        self.balance-=amount
        print("RS.",amount ,"was debited")
        print("total balance=",self.get_balance())
        
    def credit(self,amount):
        self.balance+=amount  
        print("RS.",amount,"was creadited")  
        print("total balance=",self.get_balance())

    def get_balance(self)  :
        return self.balance  

acc1=Account(10000,12345)
acc1.debit(2500)
acc1.credit(5000)
        








