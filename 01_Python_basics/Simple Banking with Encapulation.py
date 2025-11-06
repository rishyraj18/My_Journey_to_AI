class BankAccount():
    bank_name = "HDFC"

    def __init__(self,account_number, owner_name, initial_deposit):
        self.__account_number = account_number
        self.owner_name = owner_name
        self.__balance = initial_deposit
        print(f"Account created for : {self.owner_name} (Acc No : {self.__account_number})")

    @staticmethod
    def bank_policy():
        print("Minimum Balance - ₹500")
        print("Account should no be inactive for 1 year. if inactive which may lead to temprory freeze of you account")

    @classmethod
    def chng_bank(cls, nw_bank):
        cls.bank_name = nw_bank

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited : ₹ {amount:.2f}. Balance : ₹ {self.__balance:.2f}")
        else:
            print("Please enter correct amount (₹): ")

    def withdraw(self,amount):
        if amount <= 0:
            print("Please Enter correct Amount (₹)")
        elif self.__balance >= amount:  
            self.__balance -= amount      
            print(f"Withdrawn : ₹ {amount:.2f}; Balance : ₹ {self.__balance:.2f}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        print(f"Balance of you account is : ₹ {self.__balance:.2f}")

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder Name : {self.owner_name}")


print(BankAccount.bank_name)
Acc1 = BankAccount(12345 ,"Rishy Raj", 5000 )
Acc1.deposit(2000)
Acc1.withdraw(1000)
Acc1.get_balance()
Acc1.display_info()