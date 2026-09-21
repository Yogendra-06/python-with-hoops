class bank_account:
    acc_holder_name="yogendra"
    acc_no=312701000009629
    balance=163000
    
    def deposit(self):
        money=int(input("enter money: "))
        money=money+self.balance
        print(self)
        
    def withdraw(self,cash):
        cash=int(input("cash: "))
        print(cash)
        
    def check_balance(self):
        print(self.balance)
        
s=bank_account()
print(s.acc_holder_name)
print(s.acc_no)
print(s.balance)

s.check_balance()
s.deposit()
s.withdraw(160000)


        
    
