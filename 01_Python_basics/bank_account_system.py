# A simple OOP-based Banking System in Python with Savings and Current accounts,
# supporting deposits, withdrawals (with overdraft), interest addition, and bank policies.

class Account:                                              #Parent Class Account
    bank_name = "Python Bank"                               #Class Variable
    def __init__(self, account_No,holder_name, initial_deposit):
        self.__Account_no = account_No
        self.holder_name = holder_name
        self.__balance = initial_deposit
    
    def current_withdrawal(self,amount):                    #Current Account Withdrawal
        if (self.__balance) >= amount:
            self.__balance -= amount
            print(f"Amount Withdrawn ₹{amount}; Available Balance : ₹{self.__balance}")
        else:
            print("You Do not have enough Balance in you Account, Checking your OVERDRATF Balance")
            if (self.__balance - amount) > -5000:
                self.__balance -= amount
                print("You Do not Have Enough Money, Amount is dispatched from OVERDRAFT")
                print(f"Amount Withdrawn ₹{amount}; Available OVERDRAFT : ₹{self.__balance}")
            else:
                print("You Do have OVERDRAFT Balance Too, You cannot Withdraw Amount")
    
    def savings_withdrawal(self,amount):                    #Savings Account Withdrawal
        if (self.__balance) >= amount:
            self.__balance -= amount
            print(f"Amount Withdrawn ₹{amount}; Available Balance : ₹{self.__balance}")
        else:
            print("You do not have Enough Balance, You cannot Withdraw Amount")

    def deposit(self,amount):                               #Money Deposit 
        if amount > 0:
            self.__balance += amount
            print(f"Amount Deposited: ₹{amount};   Total Available Balance: ₹{self.__balance}")

        else:
            print("Deposit amount must be greater than ₹0")

    def check_balance(self):                                #Checking Balance from an Account
        print(f"HI, {self.holder_name}, your Account Balance is  ₹{self.__balance}")

    def get_account_info(self):                             #Get Account Info (Account Holder Name, Account No, Account Balance)
        print(f"\nAccount Holder Name: {self.holder_name}")
        print(f"Account No : {self.__Account_no}")
        print(f"Available Balance: ₹{self.__balance}")

    @classmethod
    def change_bank(cls, new_name):                         #Class Method to change Bank name
        cls.bank_name = new_name
        print(f"Bank Name changed to: {cls.bank_name}")

    @staticmethod 
    def bankpolicy():                                       #Static Method -  To display Bank Policy
        print("Minimum Balance = 500")
        print("Overdraft Limit: 5000 (note only for Current Account)")
        print("Interest Rate : 5% for savings account")

    @classmethod
    def show_bank_name(cls):
        print(f"🏦 Bank Name: {cls.bank_name}")


class savingsAccount(Account):                              #Child Class - Savings Account inherited from Parent Class 'Account'

    def __init__(self, account_No, holder_name, initial_deposit):
        super().__init__(account_No, holder_name, initial_deposit)
        print(f"Account Created: {holder_name}")
        print("Account Type: Saving Account")
    
    def add_interest(self):                                 #Interest calculation for Savings Account
        interest_rate = 0.05
        temp = (self._Account__balance * interest_rate)
        self._Account__balance += temp
        print("Interest Added to Account!")
        print(f"Interest Added = ₹ {temp}; Current Account balance is : ₹{self._Account__balance}")

    def withdrawal(self, amount):                           
        return super().savings_withdrawal(amount)


class CurrentAccount(Account):                              #Current Account - class inherited from parent class 'Account'
    def __init__(self, account_No, holder_name, initial_deposit):
        super().__init__(account_No, holder_name, initial_deposit)
        print(f"Account Created for: {holder_name} ")
        print("Account Type: Current Account")
    
    def withdrawal(self, current_amount):
        return super().current_withdrawal(current_amount)
    

acc1 = savingsAccount(12345, "Rishy Raj", 0)
acc1.deposit(2000)
acc1.add_interest()

acc2 = CurrentAccount(54321, "Rocky", 0 )
acc2.withdrawal(3000)

Account.change_bank("AI Finance Corp")