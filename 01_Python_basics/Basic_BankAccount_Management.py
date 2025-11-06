class Bankaccount():
    bank_name  = "HDFC"

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,d_amount):
        self.balance += d_amount
        print(f"Amount Deposited : {d_amount}, Current Balance : {self.balance:.2f}")
    
    def withdraw(self, w_amount):
        if self.balance >= w_amount:
            self.balance -= w_amount
            print(f"Amount withdrawn : {w_amount}, Current Balance : {self.balance:.2f}")
        else:
            print("Insufficient Balance")
    
    def display_balance(self):
        print (f"Hi {self.name}, Your account balance = {self.balance:.2f}")

    @classmethod
    def change_bank(cls, new_bank):
        cls.bank_name = new_bank
    
    @staticmethod
    def interest(amount, rate):
        print (f"Interest rate for {amount} at {rate} : {(amount * rate) / 100}")



acc1 = Bankaccount("Rishy Raj", 10000)
acc1.display_balance()
acc1.deposit(5000)
acc1.withdraw(4000)
print(f"Bank Name :{Bankaccount.bank_name}")
Bankaccount.change_bank("SBI")
print(f"Bank Name :{Bankaccount.bank_name}")
Bankaccount.interest(500000, 15)